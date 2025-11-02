from flask import Flask, render_template, request, redirect, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
from resend import Resend

load_dotenv()
secret_key = os.getenv('SECRET_KEY')

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY") or "dev-key"

resend_client = Resend(os.getenv("RESEND_API_KEY"))


@app.route("/", methods=['GET', 'POST'])
def home():
    error = None
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if not (name and email and message):
            error = "All fields are required."
        else:
            try:
                send_email(name, email, message)
                flash("Message sent. Thank you!")
                return redirect("/#contact")
            except Exception as e:
                print("Send error:", e)
                error = "Could not send message. Please try later."

        return render_template("index.html", error=error)


def send_email(name, email, message):
    receiver_email = os.getenv("EMAIL_USER")
    if not receiver_email:
        raise RuntimeError("EMAIL_USER not configured")

    subject = f"New Message from {name}"
    text = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

    return resend_client.emails.send({
        "from": f"Contact Form <no-reply@{os.getenv('MAIL_DOMAIN','example.com')}>",
        "to": [receiver_email],
        "reply_to": email,
        "subject": subject,
        "text": text,
    })


@app.route("/guess_states")
def guess_states():
    return render_template("guess_states.html")


if __name__ == '__main__':
    app.run()
