import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_welcome_email():
    # Email configuration
    sender_email = "ranjohndev@gmail.com"
    sender_password = "ecof ntiu cwsk desf"  # Update with the provided password
    recipients = ["team@blismo.com", "ranjohndev@gmail.com"]
    subject = "Welcome to Blismo - Your Ultimate Barbershop Solution!"
    message = """
    Dear Test Automation Email,

    Welcome to Blismo, your all-in-one solution for barbershops! We're thrilled to have you join our community and embark on this journey together.

    At Blismo, we understand the unique challenges faced by barbershops in managing appointments, engaging customers, and growing their business. That's why we've developed a comprehensive suite of tools to streamline your operations and enhance your customer experience.

    Here's what you can expect from Blismo:

    1. Effortless Appointment Management: Say goodbye to manual scheduling! With Blismo's intuitive online booking system, you can manage appointments seamlessly and keep your schedule organized.

    2. AI Marketing Insights: Our AI-powered marketing tools analyze customer data to provide personalized insights and recommendations, helping you target the right audience and maximize your marketing efforts.

    3. AI Receptionist: Let our virtual receptionist handle inquiries, appointment reminders, and customer communication, freeing up your time to focus on what you do best – delivering exceptional service to your clients.

    4. Waitlist Management: Never miss an opportunity to serve your customers. Blismo's waitlist feature ensures that no appointment slot goes unfilled, optimizing your barbershop's efficiency and revenue potential.

    5. Online Booking: Enable your customers to book appointments conveniently from anywhere, at any time. With our mobile-friendly online booking interface, scheduling a haircut has never been easier.

    Whether you're a seasoned barber or just starting your journey in the industry, Blismo is here to support you every step of the way. Our team is dedicated to providing you with the tools and resources you need to succeed.

    Ready to revolutionize your barbershop experience? Get started with Blismo today!

    If you have any questions or need assistance, don't hesitate to reach out to our customer support team at support@blismo.com. We're here to help!

    Once again, welcome to the Blismo family. We can't wait to see your barbershop thrive with our platform.

    Best regards,
    Ian Blachardon
    CEO, Blismo
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
        print("Welcome email successfully sent!")

    except Exception as e:
        print(f"Failed to send welcome email. Error: {e}")

    finally:
        # Close SMTP server
        server.quit()

# Send the welcome email
send_welcome_email()
