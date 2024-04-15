import logging

from flask import Flask, render_template
from gunicorn.app.base import BaseApplication

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

from flask import Flask, render_template, request
@app.route("/", methods=["GET", "POST"])
def home_route():
    if request.method == "POST":
        name = request.form["name"]
        course = request.form["course"]
        return render_template("welcome.html", name=name, course=course)
    return render_template("home.html")


class StandaloneApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.application = app
        self.options = options or {}
        super().__init__()

    def load_config(self):
        config = {
            key: value
            for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


# Do not remove the main function while updating the app.
@app.route("/selection", methods=["POST"])
def selection():
    topic = request.form["topic"]
    if topic == "sortings":
        return render_template("sorting_selection.html")
    elif topic == "algorithms":
        return render_template("algorithm_selection.html")
    elif topic == "motion-detection":
        return render_template("motion_detection.html")
    else:
        return "The selected option is not available.", 404

@app.route("/feedback", methods=["GET"])
def feedback():
    return render_template("feedback.html")

@app.route("/about-us", methods=["GET"])
def about_us():
    return render_template("about_us.html")

@app.route("/ask-us", methods=["GET"])
def ask_us():
    return render_template("ask_us.html")

@app.route("/motion-detection", methods=["GET"])
def motion_detection():
    return render_template("motion_detection.html")

if __name__ == "__main__":
    options = {"bind": "%s:%s" % ("0.0.0.0", "8080"), "workers": 4, "loglevel": "info", "accesslog": "-"}
    StandaloneApplication(app, options).run()