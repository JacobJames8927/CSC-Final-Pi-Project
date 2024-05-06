Idea:
Make a device to track the average daily traffic in a given building.

Method:
Ping Ultrasonic sensors on the inside of all exterior doors are used to track how many times a person passes through the door. Dividing this number by 2 (each person enters and exits) will track the number of people visiting the building that day (everyone leaves by the end of the day). 

User Interface:
There is one GUI that displays how many people visited the associated building and prompts the user to assign that value to the corresponding day of the week. Another GUI allows the user to create a page for each building being monitored where the building's data (how many people visited each day of the week) is displayed.

Instructions:
- Download all files/folders to a new desktop folder
- Open "Hardware Code", "Ping_Sensor", "Ping_Toggle.ino"
- Run "Ping_Toggle.ino" to start sensor tracking
- Stop running code at the end of the collection period (typically the end of the day)
- Open "PROJECT FILES", "GUI Code", "storage.py"
- Run "storage.py" (you may need to download some external libraries) to set what day data was collected
- Once data for all days have been collected, open "PROJECT FILES", "GUI Code", "GUI.py"
- Run "GUI.py"
- Add a new room, name it, and paste the path to the "population_data.py" into the data entry box
- Press Submit
