import datetime
import tkinter as tk
from tkinter import filedialog

def get_time_gaps(filepath):
    # Open the log file and read its contents
    with open(filepath, 'r') as log_file:
        log_contents = log_file.read()

    # Split the log contents into lines
    log_lines = log_contents.split('\n')

    # Initialize a variable to store the previous timestamp
    prev_timestamp = None

    # Iterate through each line of the log
    for line in log_lines:
        # Try to find a timestamp in the line
        timestamp_start = line.find('[')
        timestamp_end = line.find('Z')
        if timestamp_start != -1 and timestamp_end != -1:
            timestamp = line[timestamp_start+1:timestamp_end+1]

            # If we have a previous timestamp, calculate the time gap
            if prev_timestamp:
                time_gap = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ') - datetime.datetime.strptime(prev_timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
                if time_gap > datetime.timedelta(minutes=30):
                    print(f'Time gap of {time_gap} between timestamps')
            # Update the previous timestamp
            prev_timestamp = timestamp

def main():
    root = tk.Tk()
    root.withdraw()

    filepath = filedialog.askopenfilename(filetypes=[("Log files", "*.log")])
    get_time_gaps(filepath)

if __name__ == '__main__':
    main()
