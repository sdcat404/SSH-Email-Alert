import os
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Constants
LOG_FILE = "/var/log/auth.log"  # SSH log file location on Server
EMAIL_ADDRESS = "your_email@gmail.com"  # Your Gmail address
EMAIL_PASSWORD = "your_app_password"  # App Password generated for Gmail
TO_EMAIL = "recipient_email@example.com"  # Recipient's email address
MAIL_SUBJECT = "SSH Alert"

def send_email(subject, message, to_email):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "plain"))

        server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
        server.quit()
        print("Email notification sent successfully.")
    except Exception as e:
        print("Failed to send email:", str(e))

def monitor_ssh_log():
    try:
        with open(LOG_FILE, "r") as log_file:
            log_file.seek(0, os.SEEK_END)
            while True:
                line = log_file.readline()
                if not line:
                    time.sleep(1)
                    continue
                if "sshd" in line and ("Accepted" in line or "Failed" in line):
                    send_email(MAIL_SUBJECT, f"SSH login detected on Server:\n{line}", TO_EMAIL) #Change "server" to your IP or host name
    except Exception as e:
        print("Error reading SSH log file:", str(e))

if __name__ == "__main__":
    print("SSH monitoring script is running...")
    monitor_ssh_log()
