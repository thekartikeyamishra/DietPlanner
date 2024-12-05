# Personalized Diet Planner

For the next 15 days, I'll be creating and sharing 15 projects – one per day! Free versions will be open to all on my GitHub, and a low-cost paid version will be available too. Can't wait to hear your thoughts!

A **Personalized Diet Planner** is a Python-based application that helps users create meal plans based on their daily calorie target. It provides a simple graphical user interface (GUI) for user interaction and basic meal recommendations from a predefined dataset.

---

## Features

- **Enter Calorie Target**: Users can input their desired daily calorie target.
- **Generate Meal Plan**: The app provides a list of meals that fit within the specified calorie range.
- **Simple GUI**: A user-friendly interface built using `Tkinter`.
- **Predefined Meal Dataset**: Uses a sample dataset (`sample_meals.csv`) with meal names and their calorie values.

---

## Project Structure

```
DietPlanner/
├── data/                     
│   ├── sample_meals.csv      # Predefined dataset with meal details
├── gui/                      
│   ├── __init__.py           # Makes the folder a Python package
│   ├── diet_gui.py           # GUI implementation
├── utils/                    
│   ├── __init__.py           # Makes the folder a Python package
│   ├── diet_logic.py         # Backend logic for meal plan generation
├── main.py                   # Entry point for the application
```

---

## Installation and Setup

Follow these steps to run the project locally:

### Prerequisites
- Python 3.8 or higher installed on your system.
- `pip` (Python package manager).

### Clone the Repository
```bash
git clone https://github.com/thekartikeyamishra/DietPlanner.git
cd DietPlanner
```

### Set Up Virtual Environment (Optional but Recommended)
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Install Dependencies
```bash
pip install pandas
```

---

## How to Run

1. Navigate to the project directory.
2. Run the application:
   ```bash
   python main.py
   ```

3. A GUI window will appear. Enter your daily calorie target and click on "Generate Meal Plan" to see the recommended meals.

---

## Example

### Input:
- **Calorie Target**: 400 kcal

### Output:
```
Meal Plan:
Oatmeal - 300 kcal
Chicken Salad - 400 kcal
Vegetable Stir-Fry - 350 kcal
```

---

## Dataset Details

The predefined dataset is stored in `data/sample_meals.csv` and includes the following columns:
- **Meal**: Name of the meal.
- **Calories**: Calorie value of the meal.

---

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Create a pull request.


---

## Contact

For questions or suggestions, feel free to reach out:
- **Author**: Kartikeya Mishra
- **Email**: workmailkartikeya@gmail.com
