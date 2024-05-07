import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import requests

def send_welcome_email():
    # Email configuration
    sender_email = "ranjohndev@gmail.com"
    sender_password = "ecof ntiu cwsk desf"  # Update with the provided password
    recipients = ["test@blismo.com", "ranjohndev@gmail.com"]
    subject = "Welcome to Blismo - Your Ultimate Barbershop Solution!"
    message = """
    <html>
    <body>
        <p>Dear Test Automation Email,</p>
        <p>Welcome to Blismo, your all-in-one solution for barbershops! We're thrilled to have you join our community and embark on this journey together.</p>
        <p>At Blismo, we understand the unique challenges faced by barbershops in managing appointments, engaging customers, and growing their business. That's why we've developed a comprehensive suite of tools to streamline your operations and enhance your customer experience.</p>
        <p>Here's what you can expect from Blismo:</p>
        <ol>
            <li>Effortless Appointment Management: Say goodbye to manual scheduling! With Blismo's intuitive online booking system, you can manage appointments seamlessly and keep your schedule organized.</li>
            <li>AI Marketing Insights: Our AI-powered marketing tools analyze customer data to provide personalized insights and recommendations, helping you target the right audience and maximize your marketing efforts.</li>
            <li>AI Receptionist: Let our virtual receptionist handle inquiries, appointment reminders, and customer communication, freeing up your time to focus on what you do best – delivering exceptional service to your clients.</li>
            <li>Waitlist Management: Never miss an opportunity to serve your customers. Blismo's waitlist feature ensures that no appointment slot goes unfilled, optimizing your barbershop's efficiency and revenue potential.</li>
            <li>Online Booking: Enable your customers to book appointments conveniently from anywhere, at any time. With our mobile-friendly online booking interface, scheduling a haircut has never been easier.</li>
        </ol>
        <p>Whether you're a seasoned barber or just starting your journey in the industry, Blismo is here to support you every step of the way. Our team is dedicated to providing you with the tools and resources you need to succeed.</p>
        <p>Ready to revolutionize your barbershop experience? Get started with Blismo today!</p>
        <p>If you have any questions or need assistance, don't hesitate to reach out to our customer support team at <a href="mailto:support@blismo.com">support@blismo.com</a>. We're here to help!</p>
        <p>Once again, welcome to the Blismo family. We can't wait to see your barbershop thrive with our platform.</p>
        <p>Best regards,<br>Ian Blachardon<br>CEO, Blismo</p>
        <p><b>P.S. Check out this cool barbershop GIF:</b></p>
        <img src="cid:barbershop_gif">
    </body>
    </html>
    """

    # Fetch the GIF from URL and create MIMEImage object
    gif_url = "https://media.giphy.com/media/l4hmNco31StLkZfJC/giphy.gif"
    response = requests.get(gif_url)
    if response.status_code == 200:
        gif_data = response.content
        gif = MIMEImage(gif_data)
        gif.add_header('Content-Disposition', 'inline', filename="barbershop.gif")
        gif.add_header('Content-ID', '<barbershop_gif>')
    else:
        print("Failed to fetch the GIF from URL")

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = subject

    # Add message body
    msg.attach(MIMEText(message, 'html'))

    # Attach GIF
    msg.attach(gif)

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
