import csv
from datetime import datetime
import os

def check_decimal(number):
  if "," in str(number):
    # Replace the "," with a "."
    number = number.replace(",", ".")
  return float(number)

def track_weight(weight_input, fat_input, muscle_input):
  

    try:
        weight = check_decimal(weight_input)
        body_fat = check_decimal(fat_input)
        muscle_mass = check_decimal(muscle_input)
    except:
        return "Please write a number"

    # Get today's date
    today = datetime.now().strftime("%Y-%m-%d")

    # Check if the CSV file exists
    if not os.path.exists('weight_tracker.csv'):
        # Create the CSV file and add a header row
        with open('weight_tracker.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Weight', 'Body Fat', 'Muscle Mass'])

    else:
        # Open the CSV file in read mode
        with open('weight_tracker.csv', 'r') as file:
            # Create a CSV reader
            reader = csv.reader(file)
            # Skip the header row
            next(reader)

            # Check if a weight has already been recorded for today's date
            for row in reader:
                if row[0] == today:
                    return("A weight has already been recorded for today.")

    # Open the CSV file in append mode
    with open('weight_tracker.csv', 'a', newline='') as file:
        # Create a CSV writer
        writer = csv.writer(file)
        # Add the current weight and date to the CSV file
        writer.writerow([today, weight, body_fat, muscle_mass])
        return(weight,today)

track_weight("87,9", "7", "28.2")