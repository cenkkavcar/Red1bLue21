import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time

# Email configuration
sender_email = 'sender@gmail.com'  # Your email
receiver_email = 'receiver@gmail.com'  # Same email for testing
password = 'App Password'  # Use the generated app password

subject = 'Hello World'
body = 'Sent with Python Script'

# Track the number of sent emails
email_count = 0
max_emails = 5  # Stop after 5 emails

def send_email():
    global email_count
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, password)  # Login to your email account
            server.send_message(msg)  # Send the email
        email_count += 1
        print(f'Email {email_count} sent successfully!')

    except Exception as e:
        print(f'Error occurred: {e}')

    # Stop the schedule after sending 5 emails
    if email_count >= max_emails:
        print('Reached the maximum number of emails. Stopping...')
        return schedule.CancelJob

# Schedule the task to run every 1 minute
schedule.every(1).minutes.do(send_email)

# Keep the script running and stop after 5 emails
while email_count < max_emails:
    schedule.run_pending()
    time.sleep(1)

print("Script stopped after sending 5 emails.")
