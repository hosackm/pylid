from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", status=True)


# Use special routes for debugging
@app.route("/status/<on_off>")
def status(on_off):
    if on_off == "1":
        return render_template("index.html", status=True)
    else:
        return render_template("index.html", status=False)

if __name__ == "__main__":
    app.run(debug=True)
