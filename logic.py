def calculate_bmi(height_cm, weight_kg):
    
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)
def get_bmi_category(bmi):
    
    if bmi < 18.5:
        return "Underweight", "May indicate insufficient calorie intake."
    elif bmi < 25:
        return "Normal", "Generally considered a healthy weight."
    elif bmi < 30:
        return "Overweight", "May increase risk of lifestyle-related issues."
    else:
        return "Obese", "Higher health risk, balanced diet advised."