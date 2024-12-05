import pandas as pd
import random

def generate_csv():
    # Generate sample data
    meals = [
        "Oatmeal", "Chicken Salad", "Grilled Salmon", "Vegetable Stir-Fry",
        "Pasta", "Egg Sandwich", "Fruit Smoothie", "Turkey Wrap",
        "Beef Stew", "Caesar Salad", "Quinoa Bowl", "Shrimp Tacos",
        "Veggie Pizza", "Burrito", "Roasted Chicken", "Tofu Stir-Fry",
        "Mushroom Risotto", "Avocado Toast", "Grilled Cheese", "Sushi",
        "Pancakes", "French Toast", "Cereal", "Yogurt Parfait",
        "Fish Curry", "Lamb Chops", "Vegetable Soup", "Stuffed Peppers",
        "Falafel Wrap", "Chickpea Salad", "Bean Chili", "Veggie Burger",
        "Fried Rice", "Pad Thai", "Dumplings", "Ramen",
        "Chicken Curry", "Spinach Quiche", "Cheese Omelette", "Turkey Meatballs"
    ]

    # Generate 1000 sample meal entries
    data = {
        "Meal": [random.choice(meals) for _ in range(1000)],
        "Calories": [random.randint(200, 700) for _ in range(1000)]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Save to CSV
    df.to_csv("data/sample_meals.csv", index=False)
    print("sample_meals.csv created successfully in the 'data' folder.")

if __name__ == "__main__":
    generate_csv()
