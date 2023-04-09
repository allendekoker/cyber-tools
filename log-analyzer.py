import re

def analyze_log_file(log_file_path):
    # Read the log file
    with open(log_file_path, 'r') as log_file:
        log_content = log_file.read()

    # Extract each log entry using a regular expression
    log_entries = re.findall(r'(\[[^\]]+\]) (\S+) (.+)', log_content)

    # Count the number of occurrences of each log entry
    log_entry_counts = {}
    for entry in log_entries:
        if entry in log_entry_counts:
            log_entry_counts[entry] += 1
        else:
            log_entry_counts[entry] = 1

    # Sort the log entries by their occurrence count
    sorted_log_entries = sorted(log_entry_counts.items(), key=lambda x: x[1], reverse=True)

    # Print out the log entries and their occurrence counts
    for entry, count in sorted_log_entries:
        print(f'{entry}: {count}')
