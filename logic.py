def calculate_bmi(height_cm, weight_kg):
    
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)
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