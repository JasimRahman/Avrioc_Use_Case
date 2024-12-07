from kafka import KafkaConsumer
import json
from pymongo import MongoClient

# MongoDB Configuration
client = MongoClient('localhost', 27017)
db = client['user_data']
collection = db['aggregations']

# Kafka Consumer configuration
consumer = KafkaConsumer(
    'user_interactions',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

user_interactions = {}

for message in consumer:
    data = message.value
    user_id = data['user_id']
    item_id = data['item_id']

    # Update user interactions
    if user_id not in user_interactions:
        user_interactions[user_id] = 0
    user_interactions[user_id] += 1

    # Calculate average interactions per user
    avg_interactions = sum(user_interactions.values()) / len(user_interactions)

    # Store data in MongoDB
    collection.update_one(
        {"user_id": user_id},
        {"$set": {"average_interactions": avg_interactions}},
        upsert=True
    )

    print(f"Processed: {data}, Updated Avg: {avg_interactions}")
