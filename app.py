
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    print("NEW CONTACT MESSAGE")
    print("Name:", name)
    print("Email:", email)
    print("Message:", message)

    return f"""
    <h1>Thank you, {name}!</h1>
    <p>Your message was received.</p>
    <a href="/">Return to Home</a>
    """

if __name__ == "__main__":
    app.run(debug=True)
