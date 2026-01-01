from flask import Flask, render_template, request
from logic import (
    calculate_bmi,
    get_bmi_category,
    calculate_daily_calories,
    generate_meal_plan,
    calculate_total_calories,
    load_foods
)

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
    activity = request.form.get("activity")

    hemoglobin = float(request.form["hemoglobin"])

    bmi = calculate_bmi(height, weight)
    category, explanation = get_bmi_category(bmi, age, gender)

    daily_calories = calculate_daily_calories(weight, activity)
    user_data = {
        "bmi": bmi,
        "hemoglobin": hemoglobin,
        "calories": daily_calories
    }
    foods = load_foods()
    print(user_data)
    print(foods)
    meal_plan = generate_meal_plan(user_data, foods)
    total_calories = calculate_total_calories(meal_plan)
    print(meal_plan)
    return render_template(
        "result.html",
        bmi=bmi,
        category=category,
        explanation=explanation,
        daily_calories=daily_calories,
        meal_plan=meal_plan,
        total_calories=total_calories
    )


if __name__ == "__main__":
    app.run(debug=True)
