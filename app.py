from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Home page showing resume
@app.route("/")
def resume():
    return render_template("resume.html")

# Download resume PDF
@app.route("/download")
def download_resume():
    return send_from_directory(
        directory=os.getcwd(),
        path="resume.pdf",
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True)