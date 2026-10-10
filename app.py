from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Read the eight values submitted by the user
        features = [
            float(request.form["MedInc"]),
            float(request.form["HouseAge"]),
            float(request.form["AveRooms"]),
            float(request.form["AveBedrms"]),
            float(request.form["Population"]),
            float(request.form["AveOccup"]),
            float(request.form["Latitude"]),
            float(request.form["Longitude"])
        ]

        # Temporary demonstration calculation.
        # Replace this with your trained ML model later.
        prediction = "Inputs received successfully!"

        return render_template(
            "index.html",
            prediction_text=prediction
        )

    except (ValueError, KeyError):
        return render_template(
            "index.html",
            prediction_text="Please enter valid values in every field."
        )


if __name__ == "__main__":
    app.run(debug=True)