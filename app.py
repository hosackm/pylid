from flask import Flask, render_template
from camera import Camera

app = Flask(__name__)
cam = Camera()


@app.route("/")
def index():
    return render_template("index.html", status=True)


@app.route("/camera")
def camera():
    cam.grab_frame()
    cam.save_frame("default.jpg")
    return render_template("camera.html")


if __name__ == "__main__":
    app.run(debug=True)
