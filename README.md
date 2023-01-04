# weight_tracker
Streamlit app to input weight data and get visualisations

Streamlit is used to provide front-end and data visualisation. The backend is centered around the 'track_weight' function of the weight tracking app. The function takes three inputs: weight_input, fat_input, and muscle_input. These represent the user's current weight, body fat percentage, and muscle mass, respectively.

The function first checks if the input values contain a decimal point (",") and replaces it with a period (".") if necessary. It then attempts to convert the input values to floats and returns an error message if this is unsuccessful.

The function then gets the current date and checks if a weight_tracker.csv file already exists. If the file does not exist, the function creates it and adds a header row. If the file does exist, the function opens it in read mode and checks if the current date has already been recorded. If the date has already been recorded, the function returns an error message. If the date has not been recorded, the function opens the weight_tracker.csv file in append mode and writes the current date, weight, body fat percentage, and muscle mass to the file. Finally, the function returns a string containing a summary of the data recorded.
