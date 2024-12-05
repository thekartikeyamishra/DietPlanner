import pandas as pd


def generate_meal_plan(calories):
    try:
        # Load the CSV file
        df = pd.read_csv("data/sample_meals.csv")

        # Ensure column names are correct
        if "Meal" not in df.columns or "Calories" not in df.columns:
            raise KeyError("CSV file must contain 'Meal' and 'Calories' columns.")

        # Filter meals within calorie range
        selected_meals = df[df["Calories"] <= calories]
        if selected_meals.empty:
            return "No meals available within this calorie range."

        # Build the result string
        result = "Meal Plan:\n"
        for _, row in selected_meals.iterrows():
            result += f"{row['Meal']} - {row['Calories']} kcal\n"
        return result
    except Exception as e:
        return f"Error: {e}"
