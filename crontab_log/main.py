import datetime

# Open the log file in append mode
with open('/mnt/d/Files/Programming/100 Days of Code Python/crontab_log/log.txt', 'a') as f:
    # Get the current date and time
    now = datetime.datetime.now().strftime("%B %d, %Y %I:%M %p")
    # Write the date and time to the log file
    f.write(f'Script ran at {now}\n')
