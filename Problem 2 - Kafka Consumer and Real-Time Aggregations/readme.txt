# Problem 2: Kafka Consumer and Real-time Aggregations

## Purpose:
This script consumes user interaction data from a Kafka topic, performs real-time aggregations (e.g., average interactions per user, max/min interactions per item), and stores the results in a NoSQL database.

## How to Run:

### 1. Set up Kafka Consumer:
Ensure Kafka is running and that the producer from Problem 1 is publishing data to the `user_interaction_topic`.

### 2. Choose NoSQL Database:
This implementation uses [MongoDB](https://www.mongodb.com/) as the NoSQL database. You may opt for other databases like Elasticsearch or Cassandra based on your preference.

### 3. Database Setup:
Set up MongoDB either locally or on the cloud. The script will connect to MongoDB and store aggregated results in a collection named `aggregated_interactions`.

### 4. Running the Kafka Consumer:
Run the following command to start consuming data, perform aggregation, and insert the results into MongoDB:
```bash
python kafka_consumer.py

Aggregation Operations:
Average Interactions per User: Calculating the average number of interactions by each user.
Maximum and Minimum Interactions per Item: Identifying the maximum and minimum interactions for each item.

MongoDB Schema:
The aggregation data is stored in the following format:

{
  "user_id": "user_123",
  "avg_interactions": 10,
  "item_id": "item_456",
  "max_interactions": 50,
  "min_interactions": 1
}

Dependencies:
kafka-python
pymongo
json


Install dependencies using:

pip install -r requirements.txt