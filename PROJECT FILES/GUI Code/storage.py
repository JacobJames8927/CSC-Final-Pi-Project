import serial
import threading
import re
from time import sleep
import tkinter as tk
import json
from math import ceil


SERIAL_PORT = 'COM7'
BAUD_RATE = 9600
population_per_day = {
    "Sunday": 0,
    "Monday": 0,
    "Tuesday": 0,
    "Wednesday": 0,
    "Thursday": 0,
    "Friday": 0,
    "Saturday": 0
}
population_today = 0
ser = None  # Global variable to hold the serial port

def save_population_data():
    with open('population_data.py', 'w') as file:
        json.dump(population_per_day, file)

def load_population_data():
    try:
        with open('population_data.py', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return population_per_day

def on_submit():
    print("Submit button clicked")
    day = day_entry.get().capitalize()
    if day in population_per_day:
        population_per_day[day] = population_today
        population_label.config(text=str(population_today))
        save_population_data()  # Save the updated dictionary
        print(population_per_day)

# Load the population data from the file
population_per_day.update(load_population_data())

current_pop = load_population_data()


try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

    root = tk.Tk()
    root.title("Population Input")

    day_label = tk.Label(root, text="Day:")
    day_label.grid(row=0, column=0, padx=5, pady=5)

    day_entry = tk.Entry(root)
    day_entry.grid(row=0, column=1, padx=5, pady=5)

    count_label = tk.Label(root, text="Population Today:")
    count_label.grid(row=1, column=0, padx=5, pady=5)

    population_label = tk.Label(root, text=str(population_today))
    population_label.grid(row=1, column=1, padx=5, pady=5)

    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.grid(row=2, columnspan=2, padx=5, pady=5)

    def read_initial_population():
        global population_today
        if ser:
            max_pop_today = ser.readline().decode().strip()
            data = ceil(int(max_pop_today) / 2)
            population_today = int(data)
            population_label.config(text=str(population_today))  # Update population label with initial value

    read_initial_population()

    root.mainloop()

except Exception as e:
    print("An error occurred:", e)

finally:
    if ser:
        ser.close()
