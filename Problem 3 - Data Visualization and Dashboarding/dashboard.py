import streamlit as st
import pandas as pd
from pymongo import MongoClient

def fetch_data():
    # Fetch data from MongoDB, excluding the _id field
    client = MongoClient('localhost', 27017)
    db = client['user_data']
    collection = db['aggregations']
    data = list(collection.find({}, {'_id': 0}))
    return pd.DataFrame(data)

def main():
    st.title("Real-Time Interaction Dashboard")

    # Streamlit auto-refresh mechanism
    st.write("Metrics Overview")
    
    # Fetch and display data
    df = fetch_data()

    if not df.empty:
        st.dataframe(df)

        # Display metrics
        st.metric("Average Interactions (Overall)", df["average_interactions"].mean())

        # Example line chart visualization
        if "timestamp" in df.columns and "average_interactions" in df.columns:
            df["timestamp"] = pd.to_datetime(df["timestamp"])  # Ensure timestamp is in datetime format
            df = df.sort_values("timestamp")  # Sort by time for proper chart visualization
            st.line_chart(data=df.set_index("timestamp")["average_interactions"])
    else:
        st.warning("No data available in the database.")

# This ensures the app runs correctly
if __name__ == "__main__":
    main()
