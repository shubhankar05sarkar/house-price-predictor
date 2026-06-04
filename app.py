from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("house_model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":

        overall_qual = int(request.form["overallqual"])
        gr_liv_area = float(request.form["grlivarea"])
        garage_cars = int(request.form["garagecars"])
        garage_area = float(request.form["garagearea"])
        total_bsmt_sf = float(request.form["totalbsmtsf"])
        full_bath = int(request.form["fullbath"])
        bedrooms = int(request.form["bedrooms"])
        year_built = int(request.form["yearbuilt"])

        input_data = [[
            overall_qual,
            gr_liv_area,
            garage_cars,
            garage_area,
            total_bsmt_sf,
            full_bath,
            bedrooms,
            year_built
        ]]

        prediction = model.predict(input_data)[0]

        prediction = round(prediction)

    return render_template(
        "index.html",
        prediction=prediction
    )

if __name__ == "__main__":
    app.run(debug=True)