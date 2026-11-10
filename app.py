
from flask import Flask
import os

app = Flask(__name__)
visits = 0

@app.route("/")
def home():
    global visits
    visits += 1

    return f"""
    <html>
    <body style="font-family:Arial;text-align:center;padding:40px">
        <h1>Cyber Security Lab</h1>
        <h2>Welcome!</h2>
        <p>This is an educational security demo.</p>
        <p>No personal information is collected.</p>
        <p>Demo visits: {visits}</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
