import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import requests

def send_demo_email():
    # Email configuration
    sender_email = "ranjohndev@gmail.com"
    sender_password = "ecof ntiu cwsk desf"  # Update with the provided password
    recipients = ["team@blismo.com", "ranjohndev@gmail.com"]
    subject = "Schedule a Demo for Blismo Software"
    
    # Load the GIF image
    gif_url = "https://media.giphy.com/media/9iCp3hK2jLT10x1eMd/giphy.gif"
    response = requests.get(gif_url)
    image_data = response.content

    # Create a MIMEImage object for the GIF
    image = MIMEImage(image_data, name="blismo_demo.gif")

    # Create the HTML message with the GIF
    message = f"""
    <html>
        <body>
            <p>Dear Team,</p>

            <p>I hope this email finds you well.</p>

            <p>My name is Ian  from Blismo, and I am reaching out to schedule a demo for our innovative barbershop management software. Blismo offers a comprehensive solution designed to streamline operations, enhance customer experience, and maximize revenue for barbershops of all sizes.</p>

            <p>During the demo, we will walk you through the key features of Blismo and demonstrate how our software can benefit your barbershop business. The demo will last approximately 30 minutes, and we can schedule it at your convenience.</p>

            <p>Please let me know your availability for the demo, and I will arrange the meeting accordingly. You can reply to this email or contact me directly at [Your Contact Information].</p>

            <p>Thank you for considering Blismo. We look forward to showcasing our software and discussing how it can help your barbershop thrive.</p>

            <p>Best regards,<br>
            Ian, B Sales </p>
            
            <img src="cid:blismo_demo.gif">
        </body>
    </html>
    """

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = subject

    # Attach the GIF image
    msg.attach(image)

    # Attach HTML message
    msg.attach(MIMEText(message, 'html'))

    try:
        # Set up SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send email
        server.sendmail(sender_email, recipients, msg.as_string())
        print("Demo email successfully sent!")

    except Exception as e:
        print(f"Failed to send demo email. Error: {e}")

    finally:
        # Close SMTP server
        server.quit()

# Example usage:
send_demo_email()
