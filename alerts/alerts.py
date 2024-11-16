import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_alert(subject, body):
    # Setup email details
    sender_email = "deepika@gmail.com"
    receiver_email = "security_team_deepika@gmail.com"
    password = "trapmind"
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    # Sending the email
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()

def send_attack_alert(attack_details):
    subject = "Critical Attack Alert"
    body = f"An attack has been detected:\n\n{attack_details}"
    send_alert(subject, body)
