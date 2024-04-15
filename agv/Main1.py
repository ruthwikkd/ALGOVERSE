import logging

from flask import Flask, render_template
from werkzeug.middleware.proxy_fix import ProxyFix

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

from flask import Flask, render_template, request
@app.route("/", methods=["GET", "POST"])
def home_route():
    if request.method == "POST":
        name = request.form["name"]
        course = request.form["course"]
        return render_template("welcome.html", name=name, course=course)
    return render_template("home.html")

@app.route("/selection", methods=["POST"])
def selection():
    topic = request.form["topic"]
    if topic == "sortings":
        return render_template("sorting_selection.html")
    elif topic == "algorithms":
        return render_template("algorithm_selection.html")
    elif topic == "motion-detection":
        return render_template("motion_detection.html")
    elif topic == "bubble-sort":
        return redirect(url_for('static', filename='index.html'), code=302)
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
@app.route("/take-quiz", methods=["GET"])
def take_quiz():
    quiz_questions = [
        ('Which sorting algorithm has the worst-case time complexity of O(n^2)?', ['Merge Sort', 'Quick Sort', 'Insertion Sort', 'Heap Sort'], 'Insertion Sort'),
        ('Which sorting algorithm works by repeatedly swapping adjacent elements if they are in the wrong order?', ['Selection Sort', 'Bubble Sort', 'Merge Sort', 'Shell Sort'], 'Bubble Sort'),
        # Add the rest of the questions here
    ]
    return render_template("quiz.html", quiz_questions=quiz_questions)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, threaded=True)
