from confluent_kafka import Producer
import os
import pandas as pd
import json
import time

#time.sleep(60)

KAFKA_BROKER = "kafka:9092"
TOPIC = "stock_prices"

# Configure Kafka Producer
producer_config = {
    'bootstrap.servers': KAFKA_BROKER,
    'client.id': 'stock-producer'
}
producer = Producer(producer_config)

# Function to deliver messages
def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed: {err}")
    else:
        print(f"Delivered message {msg.value()} to {msg.topic()} [{msg.partition()}]")

# Read CSV files and publish to Kafka
def publish_to_kafka(dataset_dir):
    batch_size = 10000  # Flush after every 500 messages
    message_count = 0  # Counter to track messages in the current batch
    message_number = 0  # Counter to track total messages processed
    file_number = 0
    for file in os.listdir(dataset_dir):
        print(f"Processing file: {file}")
        if file.endswith("_minute.csv"):
            stock_name = file.split("_minute")[0]
            file_path = os.path.join(dataset_dir, file)
            data = pd.read_csv(file_path)        
            for _, row in data.iterrows():
                if message_number >= 20000:
                    producer.flush()
                    message_count = 0
                    message_number = 0
                    print("going to the next file")
                    break
                message_number += 1
                print(f"Processing message: {message_number}")
                message = {
                    "stock": stock_name,
                    "timestamp": row['date'],
                    "open": row['open'],
                    "high": row['high'],
                    "low": row['low'],
                    "close": row['close'],
                    "volume": row['volume']
                }
                # Produce message to Kafka
                producer.produce(TOPIC, json.dumps(message), callback=delivery_report)
                message_count += 1

                # Flush when batch size is reached
                if message_count >= batch_size:
                    producer.flush()
                    message_count = 0  # Reset the counter
            file_number += 1
            if file_number >= 3:
                break
    # Flush remaining messages after processing all files
    if message_count > 0:
        producer.flush()
        print(f"Flushed remaining {message_count} messages.")

if __name__ == "__main__":
    publish_to_kafka("/app/data")
