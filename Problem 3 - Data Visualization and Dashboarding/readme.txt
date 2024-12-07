# Problem 3: Data Visualization and Dashboarding

## Purpose:
This script retrieves aggregated interaction data from a NoSQL database and displays it in a simple dashboard. The dashboard shows metrics like:
- Average interactions per user
- Maximum and minimum interactions per item

## How to Run:

### 1. Database Setup:
Make sure that MongoDB (or another NoSQL database) contains the aggregated data from Problem 2.

### 2. Install Dependencies:
Ensure you have all the necessary libraries to run the dashboard:
pip install -r requirements.txt

3. Run the Dashboard:
To run the dashboard using Streamlit, use the following command:
streamlit run dashboard.py

Dashboard Features:
Average Interactions per User: Displays the average number of interactions per user.
Max/Min Interactions per Item: Displays the highest and lowest interactions for each item.
The dashboard updates in real-time, pulling the data from the NoSQL database and displaying the aggregated metrics.

Dependencies:
streamlit
pymongo


