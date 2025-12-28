from flask import Flask, render_template, request
from logic import calculate_bmi, get_bmi_category


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def submit():
    age = int(request.form["age"])
    gender = request.form["gender"]
    height = float(request.form["height"])
    weight = float(request.form["weight"])
    activity = request.form["activity"]
    hemoglobin = request.form["hemoglobin"]

    bmi = calculate_bmi(height, weight)
    category, explanation = get_bmi_category(bmi)

    return render_template(
        "result.html",
        bmi=bmi,
        category=category,
        explanation=explanation)

if __name__ == "__main__":
    app.run(debug=True)
