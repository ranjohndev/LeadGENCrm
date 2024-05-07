import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_thank_you_email():
    # Email configuration
    sender_email = "ranjohndev@gmail.com"
    sender_password = "ecof ntiu cwsk desf"  # Update with the provided password
    recipients = ["team@blismo.com", "ranjohndev@gmail.com"]
    subject = "Thank You for Connecting with Blismo!"
    message = """
    Dear Friend,
    
    I hope this email finds you well.
    
    I wanted to take a moment to express my sincere gratitude for connecting with Blismo, either by following us on Instagram or visiting our website. We truly appreciate your interest and support.
    
    As a token of our appreciation, I wanted to share some neat content that you might enjoy. You can find it [here](https://jameswaltersgrooming.com/).
    
    Additionally, I'd love to hear more about your experience with Blismo and how we can better serve you. Whether you have any questions, feedback, or suggestions, please don't hesitate to reach out. Your input is invaluable to us as we continue to improve and innovate.
    
    Thank you once again for your interest in Blismo. We're excited to have you as part of our community, and we look forward to connecting with you further!
    
    Best regards,
    Ian Blanchardon, CEO
    Blismo Team
    """

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = subject

    # Add message body
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Set up SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send email
        server.sendmail(sender_email, recipients, msg.as_string())
        print("Thank you email successfully sent!")

    except Exception as e:
        print(f"Failed to send thank you email. Error: {e}")

    finally:
        # Close SMTP server
        server.quit()

# Example usage:
send_thank_you_email()
