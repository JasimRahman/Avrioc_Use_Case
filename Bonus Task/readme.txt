# Bonus Task: Alerting Mechanism

## Purpose:
This task implements an alerting system to notify when certain thresholds are exceeded, such as when interaction counts for an item surpass a defined limit.

## How to Run:

### 1. Set Up Alert Thresholds:
Adjust the alert threshold parameters in the configuration section of the script. For example, set a threshold for the number of interactions on a particular item.

### 2. Run the Alerting System:
Run the Python script to monitor data and send alerts:
python alerting_system.py

3. Configure Notification Method:
You can configure how the alerts will be sent, such as through email or Slack. Set up the respective notification system (email or Slack) before running the script.

Example Alert:
If an item’s interaction count exceeds the threshold (e.g., 100 interactions), the system will send a notification to the configured service.

Dependencies:
smtplib (for email notifications)
slack-sdk (for Slack notifications, optional)