from flask import Flask, render_template, request
from f1_speed import speed as generate_speed_map
from f1_circuits import corner_map

app = Flask(__name__)

@app.route("/speed", methods=["GET", "POST"])
def speed_page():
    image_generated = False

    if request.method == "POST":
        season = int(request.form["season"])
        event = request.form["event"]
        session_type = request.form["session"]
        driver = request.form["driver"]

        generate_speed_map(season, event, session_type, driver)
        image_generated = True

    return render_template("speed.html", image_generated=image_generated)


@app.route("/corner", methods=["GET", "POST"])
def corner_page():
    image_generated = False

    if request.method == "POST":
        season = int(request.form["season"])
        event = request.form["event"]
        session_type = request.form["session"]

        corner_map(season, event, session_type)
        image_generated = True

    return render_template("corner.html", image_generated=image_generated)


@app.route("/")
def home_redirect():
    return render_template("speed.html", image_generated=False)


if __name__ == "__main__":
    app.run(debug=True)
