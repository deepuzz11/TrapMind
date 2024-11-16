import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_alert(message: str):
    """
    Sends an alert via email when a significant event (e.g., an attack) is detected.
    """
    sender_email = "deepikaprabhakaran11@gmail.com"
    receiver_email = "deepikaprabhakaran11@gmail.com"
    password = "deepika100"

    # Prepare the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "TrapMind Security Alert"

    body = f"ALERT: {message}"
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
        print("Alert sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")
