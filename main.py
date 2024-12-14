from flask import Flask, render_template, request, redirect
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()
secret_key = os.getenv('SECRET_KEY')

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key
@app.route("/", methods=['GET', 'POST'])
def home():
    error = None
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Check if all fields are filled
        if not name or not email or not message:
            error = "All fields are required."
        else:
            # Send the email
            send_email(name, email, message)
            return redirect('#contact')

    return render_template("index.html", error=error) 


def send_email(name, email, message):
    sender_email = os.getenv('EMAIL_USER')
    receiver_email = os.getenv('EMAIL_USER')
    subject = f"New Message from {name}"

    body = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"

    # Set up the email
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, os.getenv('EMAIL_PASSWORD'))
            server.send_message(msg)
    except Exception as e:
        print(f"Error: {e}")


@app.route("/guess_states")
def guess_states():
    return render_template("guess_states.html")

@app.route('/weather')
def weather():
    return render_template("weather.html")


if __name__ == '__main__':
    app.run()
