# Define the log file path
log_file_path = 'path/to/your/logfile.log'

# Define the user we are looking for
target_user = 'john_doe'

# Function to parse the log file and extract relevant messages
def parse_log_file(file_path, user):
    # List to store matched log lines
    matched_lines = []

    # Open the log file in read mode
    with open(file_path, 'r') as file:
        # Read the log file line by line
        for line in file:
            # Check if the line contains 'INFO: User ' followed by the target user
            if 'INFO: User ' + user in line:
                # If it matches, add it to the list of matched lines
                matched_lines.append(line.strip())

    return matched_lines

# Call the function and print the results
matched_logs = parse_log_file(log_file_path, target_user)
for log in matched_logs:
    print(log)
