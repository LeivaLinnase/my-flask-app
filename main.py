from flask import Flask, render_template, request, jsonify, flash
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
    if request.method == "POST":
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")
        message = data.get("message")

        if not (name and email and message):
            return jsonify({"status": "error", "message": "All fields are required."})

        try:
            send_email(name, email, message)
            return jsonify({"status": "success"})
        except Exception as e:
            print("Send error:", e)
            return jsonify({"status": "error", "message": "Could not send message. Try again later."})

    # GET request
    return render_template("index.html")


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
