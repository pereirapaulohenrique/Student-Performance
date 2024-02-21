import tkinter as tk
from tkinter import messagebox
from sklearn.linear_model import LinearRegression
import joblib


# Function to predict performance index
def predict_performance():
    try:
        # Extracting user input
        hours_studied = float(entry_hours_studied.get())
        previous_scores = float(entry_previous_scores.get())
        extracurricular_activities = float(entry_extracurricular_activities.get())
        sleep_hours = float(entry_sleep_hours.get())
        sample_question_papers = float(entry_sample_question_papers.get())

        # Predicting performance index
        performance_index = model.predict(
            [[hours_studied, previous_scores, extracurricular_activities, sleep_hours, sample_question_papers]])

        # Displaying prediction
        messagebox.showinfo("Prediction", f"Predicted Performance Index: {performance_index[0]}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values for all inputs.")


# Creating tkinter window
window = tk.Tk()
window.title("Performance Index Predictor")

# Creating labels and entry widgets for user input
tk.Label(window, text="Hours Studied:").grid(row=0, column=0, padx=5, pady=5)
entry_hours_studied = tk.Entry(window)
entry_hours_studied.grid(row=0, column=1, padx=5, pady=5)

tk.Label(window, text="Previous Scores:").grid(row=1, column=0, padx=5, pady=5)
entry_previous_scores = tk.Entry(window)
entry_previous_scores.grid(row=1, column=1, padx=5, pady=5)

tk.Label(window, text="Extracurricular Activities:").grid(row=2, column=0, padx=5, pady=5)
entry_extracurricular_activities = tk.Entry(window)
entry_extracurricular_activities.grid(row=2, column=1, padx=5, pady=5)

tk.Label(window, text="Sleep Hours:").grid(row=3, column=0, padx=5, pady=5)
entry_sleep_hours = tk.Entry(window)
entry_sleep_hours.grid(row=3, column=1, padx=5, pady=5)

tk.Label(window, text="Sample Question Papers Practiced:").grid(row=4, column=0, padx=5, pady=5)
entry_sample_question_papers = tk.Entry(window)
entry_sample_question_papers.grid(row=4, column=1, padx=5, pady=5)

# Button to trigger prediction
predict_button = tk.Button(window, text="Predict Performance Index", command=predict_performance)
predict_button.grid(row=5, columnspan=2, padx=5, pady=5)

# Loading the pre-trained model using joblib
model = joblib.load("lin_reg.pkl")

# Running the GUI
window.mainloop()
