# Mail Application
This is a simple mail application built using Python and the tkinter library for the graphical user interface (GUI) and the smtplib library for sending emails using the Simple Mail Transfer Protocol (SMTP).


## Features
- Compose Email: Enter your email address, password, recipient's email address, subject, and message in the respective fields.
- Send Email: Click on the "Send" button to send the email.
- Reset Email: Click on the "Reset" button to clear all the input fields.
- Error Handling: If any required field is left empty, an error message will be displayed.
- Success Message: If the email is sent successfully, a success message will be displayed.

## Requirements
- Python 3.x
- tkinter library (usually included with Python)
- smtplib library (usually included with Python)

## How to Use
1. Run the script using Python: `python mail_application.py`.
2. The mail application window will open.
3. Enter your email address in the "Email" field.
4. Enter your email password in the "Password" field.
5. Enter the recipient's email address in the "Recipient" field.
6. Enter the subject of the email in the "Subject" field.
7. Enter the message content in the "Message" field.
8. Click on the "Send" button to send the email.
9. If any required field is left empty, an error message will be displayed.
10. If the email is sent successfully, a success message will be displayed.
11. Click on the "Reset" button to clear all the input fields and compose a new email.
12. To exit the application, close the mail application window.

Note: This application uses the Gmail SMTP server to send emails. Make sure you have enabled "Less secure app access" in your Gmail account settings or use an app password if you have two-factor authentication enabled.

Feel free to modify and enhance the code according to your requirements. Enjoy sending emails with the mail application!
