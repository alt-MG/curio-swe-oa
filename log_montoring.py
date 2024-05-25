import sys

class LogMonitor:
    def __init__(self):
        self.logs = []

    def submit_log(self, timestamp, log_type, severity):
        self.logs.append([timestamp, log_type, severity])

    def compute_stats(self, logs):
        if len(logs) == 0:
            return (0.0, 0.0, 0.0)
        severities = [log[2] for log in logs]
        min_sev = min(severities)
        max_sev = max(severities)
        mean_sev = sum(severities) / len(severities)
        return (min_sev, max_sev, mean_sev)

    def query_by_log_type(self, log_type):
        logs = [log for log in self.logs if log[1] == log_type]
        return self.compute_stats(logs)

    def query_before_timestamp(self, timestamp):
        logs = [log for log in self.logs if log[0] < timestamp]
        return self.compute_stats(logs)

    def query_after_timestamp(self, timestamp):
        logs = [log for log in self.logs if log[0] > timestamp]
        return self.compute_stats(logs)

    def query_before_log_type_timestamp(self, log_type, timestamp):
        logs = [log for log in self.logs if log[1] == log_type and log[0] < timestamp]
        return self.compute_stats(logs)

    def query_after_log_type_timestamp(self, log_type, timestamp):
        logs = [log for log in self.logs if log[1] == log_type and log[0] > timestamp]
        return self.compute_stats(logs)

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def write_output_file(file_path, output_lines):
    with open(file_path, 'w') as file:
        file.writelines(output_lines)

def generate_input_file(file_path):
    sample_input = """1 1715744138011;INTERNAL_SERVER_ERROR;23.72
1 1715744138012;INTERNAL_SERVER_ERROR;10.17
2 INTERNAL_SERVER_ERROR
1 1715744138012;BAD_REQUEST;15.22
1 1715744138013;INTERNAL_SERVER_ERROR;23.72
3 BEFORE 1715744138011
3 AFTER 1715744138010
2 BAD_REQUEST
4 BEFORE INTERNAL_SERVER_ERROR 1715744138011
4 AFTER INTERNAL_SERVER_ERROR 1715744138010
"""
    with open(file_path, 'w') as file:
        file.write(sample_input)

def main(input_file, output_file):
    generate_input_file(input_file)  # Generate the input file

    log_monitor = LogMonitor()
    input_lines = read_input_file(input_file)
    output_lines = []

    for line in input_lines:
        parts = line.strip().split()
        command = int(parts[0])
        if command == 1:
            timestamp, log_type, severity = parts[1].split(';')
            log_monitor.submit_log(int(timestamp), log_type, float(severity))
            output_lines.append("No output\n")
        elif command == 2:
            log_type = parts[1]
            min_sev, max_sev, mean_sev = log_monitor.query_by_log_type(log_type)
            output_lines.append(f"Min: {min_sev:.6f}, Max: {max_sev:.6f}, Mean: {mean_sev:.6f}\n")
        elif command == 3:
            condition, timestamp = parts[1], int(parts[2])
            if condition == 'BEFORE':
                min_sev, max_sev, mean_sev = log_monitor.query_before_timestamp(timestamp)
            elif condition == 'AFTER':
                min_sev, max_sev, mean_sev = log_monitor.query_after_timestamp(timestamp)
            output_lines.append(f"Min: {min_sev:.6f}, Max: {max_sev:.6f}, Mean: {mean_sev:.6f}\n")
        elif command == 4:
            condition, log_type, timestamp = parts[1], parts[2], int(parts[3])
            if condition == 'BEFORE':
                min_sev, max_sev, mean_sev = log_monitor.query_before_log_type_timestamp(log_type, timestamp)
            elif condition == 'AFTER':
                min_sev, max_sev, mean_sev = log_monitor.query_after_log_type_timestamp(log_type, timestamp)
            output_lines.append(f"Min: {min_sev:.6f}, Max: {max_sev:.6f}, Mean: {mean_sev:.6f}\n")

    write_output_file(output_file, output_lines)

if __name__ == "__main__":
    input_file = 'input.txt'
    output_file = 'output.txt'
    main(input_file, output_file)
