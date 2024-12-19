# COMP_6231_finals



This repository contains a distributed systems project that utilizes Kafka for message queuing, Flink for stream processing, and Prometheus for monitoring. It demonstrates a producer-consumer model with real-time data processing and monitoring.


DATASET USED:
https://www.kaggle.com/datasets/debashis74017/algo-trading-data-nifty-100-data-with-indicators

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Folder Structure](#folder-structure)
- [Setup Instructions](#setup-instructions)
- [How to Run](#how-to-run)
- [Tasks and Features](#tasks-and-features)
- [Acknowledgments](#acknowledgments)

## Project Overview

This project implements:
1. **Kafka**: For message queueing and real-time data streaming.
2. **Flink**: For distributed stream processing.
3. **Prometheus**: For monitoring system metrics.
4. **Docker Compose**: For orchestrating the entire system.

The system includes:
- A producer generating data and sending it to Kafka topics.
- A consumer processing data from Kafka topics.
- Flink for distributed computation.
- Prometheus for monitoring and metrics collection.

## Technologies Used

- **Kafka**: Real-time data streaming platform.
- **Apache Flink**: Stream processing framework.
- **Prometheus**: Monitoring and alerting toolkit.
- **Docker & Docker Compose**: Containerization and orchestration.
- **Python**: For the producer and consumer scripts.


## Folder Structure

project/
├── resources/                # Configuration and Docker setup
│   ├── consumer.dockerfile   # Dockerfile for the consumer
│   ├── docker-compose.yml    # Docker Compose configuration
│   ├── kafka.dockerfile      # Dockerfile for Kafka
│   ├── prometheus.yml        # Prometheus configuration
│   └── flink-env             # Flink environment settings
├── src/                      # Source code for producer and consumer
│   ├── __init__.py           # Package initialization
│   ├── consumer.py           # Kafka consumer script
│   ├── producer.py           # Kafka producer script
│   └── sleep.sh              # Helper script for delays
└── README.md                 # Project documentation


1. **Clone the Repository**
   ```bash
   git clone https://github.com/Sujith-Kumar-2003/COMP_6231_finals.git
   cd COMP_6231_finals
   ```

cd resources
cd Docker
docker build -t kafka_image -f kafka.dockerfile .
docker build -t consumer_image -f consumer.dockerfile .

How to Run
Start Services with Docker Compose Run the following command in the resources directory to start all services:

docker-compose up
Producer and Consumer Scripts

Start the producer:
python src/producer.py
Start the consumer:

python src/consumer.py
Flink Tasks Deploy Flink tasks by accessing the Flink dashboard at http://localhost:<flink_port>.

Monitor with Prometheus Access Prometheus at http://localhost:<prometheus_port> for monitoring metrics.


Tasks and Features
Kafka Producer and Consumer
Producer: Generates messages and publishes them to Kafka topics.
Consumer: Listens to Kafka topics and processes messages.
Flink Stream Processing
Distributed computation for real-time data analysis.
Prometheus Monitoring
Tracks system performance and metrics.

FOR EASIER USE:
Navigate to the resources folder and run the command.

cd resources
cd Docker
docker compose up --build

Next:
Go to the created container: go to the created docker containers.

Open the kafka.consumer dockerfile and start the consumer.py

Open the flink.producer dockerfile and start the producer.py

THEN START THE PROMETHEUS docker file.

Next the Grafana file. And write the queries to see the results.
Like: stock_price

This will display the graph.






