import csv
import requests
from bs4 import BeautifulSoup
import re

# Open CSV file in append mode and specify field names
with open('companies.csv', 'a', newline='') as csvfile:
    fieldnames = ['Company Name', 'Phone Numbers', 'Email', 'Websites']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Scraping loop for pages
    for i in range(1, 2):
        # URL for each page
        url = f'https://INSERT_FULL_LINK'
        html_text = requests.get(url).text

        soup = BeautifulSoup(html_text, 'lxml')
        categories = soup.find_all('', class_='')

        # Scraping loop on each page
        for category in categories:
            company_name_tag = category.find('INSERT', class_='INSERT')
            if company_name_tag:
                company_name_link = company_name_tag.find('a')
                if company_name_link:
                    company_name = company_name_link.text.strip()
                    link = company_name_link['href']

                    # Retrieve details from the page
                    company_page_html = requests.get(link).text
                    company_soup = BeautifulSoup(company_page_html, 'lxml')

                    # Extract phone number links
                    phone_number_links = company_soup.find_all('a', href=True)
                    phone_numbers = [phone_number_link['href'].replace('tel:', '') for phone_number_link in phone_number_links if 'tel:' in phone_number_link['href']]

                    # Extract email addresses using regular expressions
                    email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
                    emails_found = re.findall(email_regex, company_page_html)

                    # Extract website URLs
                    website_links = company_soup.find_all('a', href=True)
                    websites = [website_link['href'] for website_link in website_links if website_link['href'].startswith(('http://', 'https://'))]

                    # Write data to CSV file
                    writer.writerow({'Company Name': company_name,
                                    'Phone Numbers': ', '.join(phone_numbers) if phone_numbers else 'Not found',
                                    'Email': ', '.join(emails_found) if emails_found else 'Not found',
                                    'Websites': ', '.join(websites) if websites else 'Not found'})
                    
                    # Print success message
                    print(f"Data scraped and written to CSV for {company_name}")
