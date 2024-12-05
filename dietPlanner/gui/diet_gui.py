import tkinter as tk
from tkinter import ttk
from utils.diet_logic import generate_meal_plan


class DietPlannerApp:
    def __init__(self):
        self.result_text = None
        self.calorie_input = None
        self.root = tk.Tk()
        self.root.title("Personalized Diet Planner")
        self.setup_gui()

    def setup_gui(self):
        ttk.Label(self.root, text="Enter Daily Calories Target :").grid(row=0, column=0, padx=10, pady=10)
        self.calorie_input = ttk.Entry(self.root)
        self.calorie_input.grid(row=0, column=1, padx=10, pady=10)

        self.result_text = tk.Text(self.root, height=10, width=50)
        self.result_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        ttk.Button(self.root, text="Generate Diet Plan", command=self.generate_plan).grid(row=2, column=0, columnspan=2,
                                                                                          pady=10)

    def generate_plan(self):
        calorie_target = self.calorie_input.get()
        try:
            calorie_target = int(calorie_target)
            meal_plan = generate_meal_plan(calorie_target)
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, meal_plan)
        except ValueError:
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, "Please enter the valid number!")

    def run(self):
        self.root.mainloop()
