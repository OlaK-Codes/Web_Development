import csv
import smtplib
from email.message import EmailMessage
from google_app_code import password

# Load email credentials
email_address = 'INSERT_EMAIL'           
email_password = password

# Read email addresses from CSV file and send emails
with open('emails.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row if it exists
    for row in reader:
        name, recipient_email = row  # Unpack the row into variables
        
        # Create email message
        msg = EmailMessage()
        msg['Subject'] = "INSERT_SUBJECT"
        msg['From'] = email_address
        msg['To'] = recipient_email  # Set the recipient email address
       
        # Read the content of the text file
        with open('message.txt', 'r') as file:
            file_content = file.read()
        print("Content of the text file:")
        msg_content = f'Hello {name} ,\n\n{file_content}\n\n'  # Plain text content
        
         # Set the email content
        msg.set_content(msg_content)

        # Connect to the SMTP server
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                # Start TLS connection
                smtp.starttls()

                # Send EHLO command and receive server response
                response = smtp.ehlo()

                # Check if the response code indicates success
                if response[0] != 250:
                    raise smtplib.SMTPConnectError("Failed to establish connection with the SMTP server.")
                else:
                    print("Connected to SMTP server successfully. Sending email...")

                # Login to the email account
                smtp.login(email_address, email_password)

                # Send the email
                smtp.send_message(msg)

                print(f'Email sent to {recipient_email}')

        except smtplib.SMTPConnectError as e:
            print(f"Connection error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
