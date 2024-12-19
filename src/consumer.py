from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import FlinkKafkaConsumer
from pyflink.common.serialization import SimpleStringSchema
from pyflink.common.typeinfo import Types
from pyflink.datastream import MapFunction
import json

# Kafka Settings
KAFKA_BROKER = "kafka:9092"  # Kafka broker address
INPUT_TOPIC = "stock_prices"  # Kafka topic to consume data from

# Example of a MapFunction to process the consumed data
class ProcessKafkaData(MapFunction):
    def map(self, value):
        """Process each Kafka record."""
        # Assuming the incoming data is in JSON format
        data = json.loads(value)
        # Here you can process the data further
        print(f"Processed record: {data}")
        return value  # You can return the transformed data if necessary

def main():
    # Set up the Flink environment
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)

    # Kafka consumer configuration
    properties = {
        'bootstrap.servers': KAFKA_BROKER,  # Kafka brokers
        'group.id': 'flink-consumer-group',  # Consumer group ID
    }

    # Create a Kafka consumer for the topic
    kafka_consumer = FlinkKafkaConsumer(
        topics=INPUT_TOPIC,  # Kafka topic to read from
        deserialization_schema=SimpleStringSchema(),  # Deserialize each message as a string
        properties=properties  # Kafka properties
    )

    # Add the Kafka consumer as a source in the Flink job
    stream = env.add_source(kafka_consumer)

    # Apply transformations (e.g., MapFunction)
    processed_stream = stream.map(ProcessKafkaData())  # Process each record with custom logic

    # Execute the Flink job
    env.execute("Kafka Consumer Example")

if __name__ == "__main__":
    main()
