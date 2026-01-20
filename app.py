from flask import Flask, render_template, request

app = Flask(__name__)

# HOME PAGE
@app.route("/")
def index():
    return render_template("index.html")

# ANALYZE BUTTON
@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files.get("logfile")

    if not file or file.filename == "":
        return "No file selected"

    lines = file.read().decode("utf-8").splitlines()

    error_lines = []
    for i, line in enumerate(lines, start=1):
        if "404" in line or "500" in line or "ERROR" in line.upper() or "MALFORMED" in line.upper():
            error_lines.append((i, line))

    return render_template("index.html", errors=error_lines)

if __name__ == "__main__":
    app.run(debug=True)
