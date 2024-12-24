import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Generate a random 6-digit OTP
def generate_otp():
    return random.randint(100000, 999999)

# Send OTP to the specified email
def send_otp(email, otp):
    sender_email = "your-email@gmail.com"  # Replace with your email
    sender_password = "your-email-password"  # Replace with your email password
    subject = "Your OTP for Verification"
    message = f"Your OTP for verification is: {otp}"

    # Create email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Send email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        print("OTP sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Main OTP Verification
def otp_verification():
    email = input("Enter your email: ")
    otp = generate_otp()
    send_otp(email, otp)

    # Prompt user to enter the OTP
    user_otp = int(input("Enter the OTP sent to your email: "))

    # Verify OTP
    if user_otp == otp:
        print("OTP verified successfully!")
    else:
        print("Invalid OTP. Please try again.")

# Run the OTP verification process
otp_verification()
