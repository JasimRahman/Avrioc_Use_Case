# Problem 1: Random Data Generator and Kafka Producer

## Purpose:
This script generates random user interaction data and sends it to a Kafka topic in real-time. The data includes:
- `user_id`: Unique identifier for each user
- `item_id`: Identifier for the item interacted with
- `interaction_type`: Type of interaction (e.g., click, view, purchase)
- `timestamp`: When the interaction occurred

## How to Run:

### 1. Set up Kafka:
Ensure Kafka is set up and running on your machine. Follow [Kafka's quick start guide](https://kafka.apache.org/quickstart) for instructions.

### 2. Configure Parameters:
The rate of data generation can be controlled via these parameters:
- `batch_size`: Number of records generated in each batch.
- `time_interval`: Time interval (in seconds) between each batch.
- `speed_multiplier`: A multiplier to adjust the data generation rate.

### 3. Running the Data Generator:
Run the Python script to generate and send data to Kafka:
```bash
python data_generator.py
Kafka Producer:
The Kafka topic used is user_interaction_topic.
The producer will send the data to this topic in real-time.

Dependencies:
kafka-python
random
time

Install dependencies using:

pip install -r requirements.txt