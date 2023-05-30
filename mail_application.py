import smtplib
import tkinter as tk
from tkinter import messagebox


def send_mail():
    global user_email, user_password, recipient_entry, subject_entry, message_text
    try:
        # Entries
        email = user_email.get()
        pwd = user_password.get()
        recipient = recipient_entry.get()
        subject = subject_entry.get()
        message = message_text.get("1.0", tk.END)
        if email == "" or pwd == "" or recipient == "" or subject == "" or message == "":
            messagebox.showinfo("All fields are required", fg="red")
        else:
            # Compose the email
            msg = f"Subject: {subject}\n\n{message}".format(subject, message)
            # Connect to the SMTP server
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            # Login to the email account
            server.login(email, pwd)
            # Send email
            server.sendmail(email, recipient, msg)
            messagebox.showinfo("Success", "Email sent successfully.")
    except smtplib.SMTPException:
        messagebox.showerror("Error", "Failed to send email.")
        # Disconnect from the server
        server.quit()


def reset_mail():
    # Clear the input fields
    user_email.delete(0, tk.END)
    user_password.delete(0, tk.END)
    recipient_entry.delete(0, tk.END)
    subject_entry.delete(0, tk.END)
    message_text.delete("1.0", tk.END)
    messagebox.showinfo("Success", "Email reset successfull.")


def mail_window():
    global user_email, user_password, recipient_entry, subject_entry, message_text

    # Create the main window
    root = tk.Tk()
    root.title("Mail Application")
    root.geometry("1000x1000")
    # Set the background colors
    root.configure(background='lightblue')

    # Create a frame for the content
    content_frame = tk.Frame(root, bg='lightblue')
    content_frame.pack(pady=40)

    # Create a label for the user's email
    user_email_label = tk.Label(content_frame, text="Email:", font=(
        "Arial", 12), bg='white', fg='black')
    user_email_label.grid(row=0, sticky=tk.W, padx=5, pady=5)
    # Create an entry field for the user's email
    user_email = tk.Entry(content_frame, width=80)
    user_email.grid(row=0, column=1, padx=5, pady=5)

    # Create a label for the user's password
    pwd_label = tk.Label(content_frame, text="Password:",
                         font=("Arial", 12), bg='white', fg='black')
    pwd_label.grid(row=1, sticky=tk.W, padx=5, pady=5)
    # Create an entry field for the user's password
    user_password = tk.Entry(content_frame, show="*", width=80)
    user_password.grid(row=1, column=1, padx=5, pady=5)

    # Create a label for the recipient
    recipient_label = tk.Label(content_frame, text="Recipient:", font=(
        "Arial", 12), bg='white', fg='black')
    recipient_label.grid(row=2, sticky=tk.W, padx=5, pady=5)
    # Create an entry field for the recipient
    recipient_entry = tk.Entry(content_frame, width=80)
    recipient_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a label for the subject
    subject_label = tk.Label(content_frame, text="Subject:", font=(
        "Arial", 12), bg='white', fg='black')
    subject_label.grid(row=3, sticky=tk.W, padx=5, pady=5)
    # Create an entry field for the subject
    subject_entry = tk.Entry(content_frame, width=80)
    subject_entry.grid(row=3, column=1, padx=5, pady=5)

    # Create a label for the message
    message_label = tk.Label(content_frame, text="Message:", font=(
        "Arial", 12), bg='white', fg='black')
    message_label.grid(row=4, sticky=tk.W, padx=5, pady=5)
    # Create a text area for the message
    message_text = tk.Text(content_frame, height=25, width=60)
    message_text.grid(row=4, column=1, padx=5, pady=5)

    # Create a button to send the mail
    send_button = tk.Button(content_frame, text="Send",
                            font=("Arial", 12), command=send_mail)
    send_button.grid(row=5, sticky=tk.W, padx=15, pady=5)

    # Create a button to reset the mail
    reset_button = tk.Button(content_frame, text="Reset",
                             font=("Arial", 12), command=reset_mail)
    reset_button.grid(row=5, sticky=tk.W, padx=120, pady=5)

    # Start the Tkinter event loop
    root.mainloop()


# Create the mail window
mail_window()
