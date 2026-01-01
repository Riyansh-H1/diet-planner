import json

def load_foods():
    with open("foods.json", "r") as file:
        return json.load(file)

def calculate_bmi(height_cm, weight_kg):
    
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

def score_food(food, bmi, hemoglobin):
    score = 0

    score += food["protein"] * 2

    if hemoglobin < 12:
        score += food["iron"] * 5

    if bmi < 18.5:  # underweight
        score += food["calories"] / 10
    elif bmi > 25:  # overweight
        score -= food["calories"] / 15

    return score

def get_bmi_category(bmi, age, gender):
    if age<20:
        if gender == "male":
            if bmi < 15:
                return "Underweight", "May indicate insufficient calorie intake."
            elif bmi < 20:
                return "Normal", "Generally considered a healthy weight."
            elif bmi < 25:
                return "Overweight", "May increase risk of lifestyle-related issues."
            else:
                return "Obese", "Higher health risk, balanced diet advised."
        else: # female
            if bmi < 14:
                return "Underweight", "May indicate insufficient calorie intake."
            elif bmi < 19:
                return "Normal", "Generally considered a healthy weight."
            elif bmi < 24:
                return "Overweight", "May increase risk of lifestyle-related issues."
            else:
                return "Obese", "Higher health risk, balanced diet advised."
    elif age<=60:
        if bmi < 18.5:
            return "Underweight", "May indicate insufficient calorie intake."
        elif bmi < 24.9:
            return "Normal", "Generally considered a healthy weight."
        elif bmi < 29.9:
            return "Overweight", "May increase risk of lifestyle-related issues."
        else:
            if bmi>=34.9:
                return "Obese Class I", "Significant health risk, medical advice recommended."
            elif bmi>=39.9:
                return "Obese Class II", "High health risk, medical intervention advised."
            else:
                return "Obese Class III", "Severe health risk, urgent medical attention needed."
    else:
        if bmi < 22:
            return "Underweight", "May indicate insufficient calorie intake."
        elif bmi < 27:
            return "Normal", "Generally considered a healthy weight."
        elif bmi < 30:
            return "Overweight", "May increase risk of lifestyle-related issues."
        else:
            return "Obese", "Higher health risk, balanced diet advised."
        
def calculate_daily_calories(weight, activity):
    # very simple logic for first-sem project
    if activity == "low":
        return int(weight * 30)
    elif activity == "moderate":
        return int(weight * 35)
    else:  # high activity
        return int(weight * 40)

def generate_meal_plan(user_data, foods):
    meal_plan = {
        "breakfast": [],
        "lunch": [],
        "dinner": [],
        "snacks": []
    }

    calorie_limit = user_data["calories"]
    low_hb = user_data["hemoglobin"] < 12

    for food in foods:
        score = 0

        # calorie-based heuristic
        if food["calories"] <= calorie_limit / 3:
            score += 1

        # iron-based heuristic for low hemoglobin
        if low_hb and food["iron"] >= 2:
            score += 1

        # selection condition (same logic, realistic threshold)
        if score >= 1:
            if food["category"] == "breakfast":
                meal_plan["breakfast"].append(food)
            elif food["category"] == "lunch":
                meal_plan["lunch"].append(food)
            elif food["category"] == "dinner":
                meal_plan["dinner"].append(food)
            elif food["category"] == "snacks":
                meal_plan["snacks"].append(food)

    return meal_plan



def calculate_total_calories(meal_plan):
    total = 0
    for meal in meal_plan:
        for food in meal_plan[meal]:
            total += food["calories"]
    return total
