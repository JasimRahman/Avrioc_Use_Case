from kafka import KafkaProducer
import json
import random
import time
from datetime import datetime

# Kafka Producer configuration
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_random_data():
    return {
        "user_id": random.randint(1, 1000),
        "item_id": random.randint(1, 500),
        "interaction_type": random.choice(["click", "view", "purchase"]),
        "timestamp": datetime.now().isoformat()
    }

# Generate data and send to Kafka topic
while True:
    data = generate_random_data()
    producer.send('user_interactions', value=data)
    print(f"Sent: {data}")
    time.sleep(1)  # Control the rate of data generation
