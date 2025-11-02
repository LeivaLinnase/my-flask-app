from flask import Flask, render_template, request, redirect, flash
from dotenv import load_dotenv
import os
import resend

load_dotenv()
secret_key = os.getenv('SECRET_KEY')

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY") or "dev-key"

resend.api_key = os.getenv("RESEND_API_KEY")


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
                flash("✅ Your message was sent successfully. I will reply as soon as possible!")
                return render_template("index.html", message_sent=True)
            except Exception as e:
                print("Send error:", e)
                flash("❌ Could not send message. Please try again later.")

        return render_template("index.html", error=error)

    # ✅ GET request always returns HTML
    return render_template("index.html", error=error)


def send_email(name, email, message):
    receiver = os.getenv("EMAIL_USER")

    payload = {
        "from": "Contact Form <no-reply@resend.dev>",
        "to": [receiver],
        "reply_to": email,
        "subject": f"New Message from {name}",
        "text": f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
    }

    try:
        response = resend.Emails.send(payload)
        print("Email sent:", response)
    except Exception as e:
        print("Resend error:", e)


@app.route("/guess_states")
def guess_states():
    return render_template("guess_states.html")


if __name__ == '__main__':
    app.run()
