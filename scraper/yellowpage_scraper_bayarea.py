import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def scrape_and_send():
    location = location_entry.get()
    
    # Check if location is provided
    if not location:
        messagebox.showerror("Error", "Please enter a location")
        return
    
    # Disable the button while scraping and sending
    scrape_button.config(state=tk.DISABLED)
    
    try:
        all_leads, website_leads, no_website_leads = scrape_yellow_pages(location)
        write_csv(all_leads, 'OL Blismo LeadGENCrm Cold Lead.csv')
        write_csv(website_leads, 'OL Blismo LeadGENCrm Website Qualification Leads.csv')
        send_email()
        messagebox.showinfo("Success", "Scraping and sending email completed successfully")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    # Re-enable the button after scraping and sending
    scrape_button.config(state=tk.NORMAL)

def scrape_yellow_pages(location):
    all_leads = []
    website_leads = []
    no_website_leads = []

    url = f"https://www.yellowpages.com/search?search_terms=barbershop&geo_location_terms={location}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        results = soup.find_all('div', class_='info')

        for result in results[:50]:  # Limit to 50 leads per run
            name_elem = result.find('a', class_='business-name')
            name = name_elem.text.strip() if name_elem else ""
            
            address_elem = result.find('div', class_='street-address')
            address = address_elem.text.strip() if address_elem else ""
            
            city_elem = result.find('div', class_='locality')
            city = city_elem.text.strip() if city_elem else ""
            
            phone_elem = result.find('div', class_='phones')
            phone = phone_elem.text.strip() if phone_elem else ""
            
            email_elem = result.find('div', class_='business-email')
            email = email_elem.text.strip() if email_elem else ""
            
            website_elem = result.find('a', class_='track-visit-website')
            website = website_elem['href'] if website_elem else ""

            lead = {'Name': name, 'Address': address, 'City': city, 'Phone': phone,
                    'Email': email, 'Website': website}

            if website:
                website_leads.append(lead)
            else:
                no_website_leads.append(lead)

            all_leads.append(lead)

    else:
        raise Exception(f"Failed to fetch data from Yellow Pages for {location}")

    return all_leads, website_leads, no_website_leads

def write_csv(leads, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Name', 'Address', 'City', 'Phone', 'Email', 'Website']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(leads)

def send_email():
    sender_email = "ranjohndev@gmail.com"
    sender_password = "ecof ntiu cwsk desf"  # Use a secure app password
    receiver_email = ["ranjohndev@gmail.com", "team@blismo.com"]
    subject = "Please upload into LeadGENCRm for further ranking and qualification"
    body = "Please find attached the CSV files containing the barbershop data."

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ', '.join(receiver_email)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Attach all leads CSV
    with open('OL Blismo LeadGENCrm Cold Lead.csv', 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
    attachment.close()
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename='OL Blismo LeadGENCrm Cold Lead.csv')
    msg.attach(part)

    # Attach website leads CSV
    with open('OL Blismo LeadGENCrm Website Qualification Leads.csv', 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
    attachment.close()
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename='OL Blismo LeadGENCrm Website Qualification Leads.csv')
    msg.attach(part)

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

# GUI setup
root = tk.Tk()
root.title("Yellow Pages Scraper")

location_label = tk.Label(root, text="Enter location:")
location_label.pack()

location_entry = tk.Entry(root)
location_entry.pack()

scrape_button = tk.Button(root, text="Scrape and Send Email", command=scrape_and_send)
scrape_button.pack(pady=10)

root.mainloop()
