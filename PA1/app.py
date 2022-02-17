from crypt import methods
from flask import Flask, render_template, request
# import math
import course_search as search
import schedule

app = Flask(__name__)

schedule = schedule.Schedule()
schedule.load_courses()
schedule = schedule.enrolled(range(5, 1000))  # eliminate courses with no students

@app.route("/")
def home() -> str:
    """
    home page
    :return:
    """
    return render_template("home.html")


@app.route("/results", methods=["POST"])
def results() -> str:
    """
    result page
    :return:
    """
    query_text = request.form["query"]  # Get the raw user query from home page
    specific_text = request.form['specific']
    return search.topmenu(query_text, specific_text, schedule)


@app.route('/courseTimes', methods=["POST"])
def course_times() -> str:
    """
    
    """
    query_text = request.form['query']
    alt_data = [request.form['days'], request.form['start'], request.form['end']]
    return search.topmenu(query_text, alt_data, schedule)


if __name__ == "__main__":
    app.run(debug=True, port=2400)
