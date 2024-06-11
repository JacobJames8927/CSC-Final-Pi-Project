import serial
import tkinter as tk
from json import JSONDecodeError, dump, load
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
population_today = 13
ser = None  # Global variable to hold the serial port

def save_pop_data():
    with open('population_data.py', 'w') as file:
        dump(population_per_day, file)

def load_pop_data():
    try:
        with open('population_data.py', 'r') as file:
            return load(file)
    except (FileNotFoundError, JSONDecodeError):
        return population_per_day

def on_submit():
    print("Submit button clicked")
    day = day_entry.get().capitalize()
    if day in population_per_day:
        population_per_day[day] = population_today
        population_label.config(text=str(population_today))
        save_pop_data()  # Save the updated dictionary
        print(population_per_day)

def read_initial_pop():
    global population_today
    if ser:
        max_pop_today = ser.readline().decode().strip()
        data = ceil(int(max_pop_today) / 2)
        population_today = int(data)
        population_label.config(text=str(population_today))  # Update population label with initial value


if __name__ == '__main__':

    # Load the population data from the file
    population_per_day.update(load_pop_data())

    # For debugging
    # current_pop = population_per_day
    # print(current_pop)

    # Init serial port
    # ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

    #### Main UI ####
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

    # Get initial population
    read_initial_pop()

    root.mainloop()

    if ser:
        ser.close()