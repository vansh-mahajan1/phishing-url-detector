"""
app.py - simple web page for the Phishing URL Detector (made with Flask).

How to run:
    pip install -r requirements.txt
    python3 app.py
Then open http://127.0.0.1:5000 in your browser.
"""

from flask import Flask, render_template, request
from detector import check_url

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    report = None
    if request.method == "POST":
        url = request.form.get("url", "").strip()
        if url:
            report = check_url(url)
    return render_template("index.html", report=report)


if __name__ == "__main__":
    app.run(debug=True)
