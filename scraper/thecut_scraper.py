import requests
from bs4 import BeautifulSoup
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def scrape_instagram(profile_url):
    # Send HTTP GET request to the Instagram profile page
    response = requests.get(profile_url)
    if response.status_code == 200:
        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all post URLs (limit to last 10 posts)
        post_urls = [a['href'] for a in soup.find_all('a', href=True) if '/p/' in a['href']][:10]
        
        # Create a CSV file to store the data
        with open('instagram_thecutdata.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['User_ID', 'Post_URL', 'Likes', 'Comments']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            # Visit each post URL
            for post_url in post_urls:
                post_response = requests.get('https://www.instagram.com' + post_url)
                if post_response.status_code == 200:
                    post_soup = BeautifulSoup(post_response.content, 'html.parser')
                    
                    # Extract likes count
                    likes_count = post_soup.find('meta', property='og:description').get('content').split(',')[0]
                    print("Likes:", likes_count)
                    
                    # Extract comments
                    comments = post_soup.find_all('div', class_='C4VMK')
                    comments_list = [comment.find('span').text for comment in comments]
                    print("Comments:", comments_list)
                    
                    # Write data to CSV
                    writer.writerow({'User_ID': hash(post_url), 'Post_URL': post_url, 'Likes': likes_count, 'Comments': comments_list})
                    
                    print("Data written for post:", post_url)
                    
            # Email the results
            email_results()

    else:
        print("Failed to fetch profile page")

def email_results():
    # Email configuration
    sender_email = "ranjohndev@gmail.com"
    sender_password = "ecof ntiu cwsk desf"
    receiver_emails = ["team@blismo.com", "ranjohndev@gmail.com"]
    subject = "Instagram Data The Cut"
    body = "Please find attached the CSV file containing the Instagram data."

    # Create email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ",".join(receiver_emails)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Attach the CSV file
    with open('instagram_thecutdata.csv', 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
    attachment.close()
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename= instagram_thecutdata.csv')
    msg.attach(part)

    # Send email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_emails, msg.as_string())

# Example usage
scrape_instagram('https://www.instagram.com/thecut/?hl=en')
