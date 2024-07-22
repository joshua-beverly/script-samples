import os
import shutil
import smtplib
from email.mime.text import MIMEText

# Function to check disk usage
def check_disk_usage(threshold):
    total, used, free = shutil.disk_usage("/")
    usage_percentage = (used / total) * 100
    return usage_percentage > threshold, usage_percentage

# Function to send an alert email
def send_alert_email(usage_percentage):
    from_address = "your_email@example.com"
    to_address = "alert_recipient@example.com"
    subject = "Disk Usage Alert"
    body = f"Disk usage has exceeded the threshold. Current usage: {usage_percentage:.2f}%"
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = to_address

    with smtplib.SMTP('smtp.example.com') as server:
        server.login("your_email@example.com", "your_password")
        server.sendmail(from_address, to_address, msg.as_string())

# Main function
def main():
    threshold = 80.0  # Set your threshold here
    exceeded, usage = check_disk_usage(threshold)
    if exceeded:
        send_alert_email(usage)
        print(f"Alert sent! Disk usage is at {usage:.2f}%")
    else:
        print(f"Disk usage is at {usage:.2f}%, which is below the threshold.")

if __name__ == "__main__":
    main()
