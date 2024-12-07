import smtplib
from email.mime.text import MIMEText

def send_alert(item_id, interaction_count):
    msg = MIMEText(f"Alert! Item {item_id} has {interaction_count} interactions.")
    msg['Subject'] = "Interaction Threshold Alert"
    msg['From'] = "alert@company.com"
    msg['To'] = "admin@company.com"

    with smtplib.SMTP('localhost') as server:
        server.send_message(msg)
        print(f"Alert sent for item {item_id}")