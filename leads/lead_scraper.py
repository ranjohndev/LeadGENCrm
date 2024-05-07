
import requests
from bs4 import BeautifulSoup

def scrape_yellowpages_barbershops():
    url = "https://www.yellowpages.com/search?search_terms=Barbershops&geo_location_terms=San+Francisco%2C+CA"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        listings = soup.find_all('div', class_='result')

        count = 0
        for listing in listings:
            name_elem = listing.find('h2', class_='n')
            if name_elem:
                name = name_elem.text.strip()
                address_elem = listing.find('div', class_='street-address')
                if address_elem:
                    address = address_elem.text.strip()
                    city_elem = listing.find('div', class_='locality')
                    city = city_elem.text.strip() if city_elem else ""
                    state_elem = listing.find('div', class_='region')
                    state = state_elem.text.strip() if state_elem else ""
                    zipcode_elem = listing.find('div', class_='postal-code')
                    zipcode = zipcode_elem.text.strip() if zipcode_elem else ""
                    full_address = f"{address}, {city}, {state} {zipcode}"
                    
                    phone_elem = listing.find('div', class_='phones phone primary')
                    phone = phone_elem.text.strip() if phone_elem else "Phone number not available"
                    
                    website_elem = listing.find('a', class_='track-visit-website')
                    website = website_elem['href'] if website_elem else "Website not available"

                    ranking_elem = listing.find('div', class_='result-rating')
                    ranking = ranking_elem.text.strip() if ranking_elem else "Ranking not available"

                    print(f"Name: {name}\nAddress: {full_address}\nPhone: {phone}\nWebsite: {website}\nRanking: {ranking}\n-----------------------------")

                    count += 1
                    if count >= 10:
                        break
                else:
                    print("Skipping lead without address")
            else:
                print("Skipping lead without name")
    else:
        print("Error: Unable to fetch data from Yellow Pages.")

scrape_yellowpages_barbershops()
