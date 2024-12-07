# Avrioc_Use_Case

Real-Time Data Pipeline Project
This project is a demonstration of a real-time data pipeline. It involves generating random interaction data, processing it in real-time, storing aggregated results in a NoSQL database, and visualizing the results on a dashboard.
-
How the Project Works
Generate Data: Create fake user interaction data and send it to Kafka for streaming.
Process Data: Consume the streamed data from Kafka, perform aggregations, and store the results in MongoDB.
Visualize Results: Display the aggregated data on a simple dashboard.
-------------------------------------------------------------------
Steps to Execute the Project
1. Clone the Repository
Download the project files to your computer:
bash
git clone https://github.com/JasimRahman/real_time_pipeline.git
cd real_time_pipeline
--
2. Install Required Packages
Install the necessary Python libraries:
bash
pip install -r requirements.txt

3. Set Up Kafka and MongoDB
Kafka: Ensure Kafka is running on your machine. Set up a Kafka topic (e.g., interaction_data).
MongoDB: Start MongoDB. Use the default configuration or update the connection details in config/db_config.json.

4. Run the Notebooks in Order
Follow these steps:
Step 1: Generate Data
Open and run 1_data_generator.ipynb.
This will generate fake user interaction data and send it to the Kafka topic.

Step 2: Consume and Process Data
Open and run 2_kafka_consumer.ipynb.
This will consume the data from Kafka, perform real-time aggregations, and save the results to MongoDB.

Step 3: Visualize the Results
Open and run 3_dashboard.ipynb.
This will start a dashboard to display:
Average interactions per user.
Maximum and minimum interactions per item.

Step 4 (Optional): Set Up Alerts
Open and run 4_optional_alerts.ipynb to implement alerts when certain thresholds are exceeded.

Important Notes
Make sure Kafka and MongoDB are running before starting the notebooks.
Update the configurations in config/kafka_config.json and config/db_config.json if needed.
For the dashboard, install and use Streamlit to run the dashboard script.

Example Commands for Kafka and MongoDB:-

Start Kafka:
bash
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties

Create Kafka Topic:
bash
bin/kafka-topics.sh --create --topic interaction_data --bootstrap-server localhost:9092

Start MongoDB:
bash
mongod
