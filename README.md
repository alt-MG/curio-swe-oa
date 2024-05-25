# curio-swe-oa

Error Log Monitoring Problem

**Description**

This repository offers a solution for an Error Log Monitoring platform, capable of processing log entries and performing various operations such as computing statistics based on timestamps and log types. The project, implemented in Python, includes functionality for generating test input files and Dockerizing the solution for easy deployment.

**Features**

1. Submit Log Entry: Store a new log entry with timestamp, log type, and severity.
2. Compute Statistics by Log Type: Calculate the min, max, and mean severity for a specified log type.
3. Compute Statistics Before/After Timestamp: Determine the min, max, and mean severity for all log entries before or after a specified timestamp.
4. Compute Statistics by Log Type and Timestamp: Calculate the min, max, and mean severity for all log entries of a specified log type occurring before or after a specified timestamp.

**Assumptions**

1. Timestamps are provided in ascending order.
2. Log types can be any UTF-8 supported string, with a maximum length of 100 characters.
3. Severity is a positive, non-zero floating-point number.
4. The solution ensures precision to 10^-6 for severity results.

**File Structure**

1. index.py: Main script for processing log entries and generating the output.
2. generate_inputs.py: Script for generating test input files.
3. input.txt: Input file containing log entries and commands.
4. output.txt: Output file for storing the results.
5. Dockerfile: Dockerfile for containerizing the application.
   
**Prerequisites**

* Python 3.8-slim
* Docker

**Running the Solution**

* Generate Test Input File: python generate_inputs.py
* Run the Main Script: python index.py

**Dockerizing the Solution**

* Build the Docker Image: docker build -t errorlogmonitoring .
* Run the Docker Container: docker run --name errorlogmonitoring -v C:/path/to/your/project/input.txt:/app/input.txt -v C:/path/to/your/project/output.txt:/app/output.txt errorlogmonitoring

**Example**

**Sample Input (input.txt):**

1 1715744138011;INTERNAL_SERVER_ERROR;23.72 <br />
1 1715744138012;INTERNAL_SERVER_ERROR;10.17 <br />
2 INTERNAL_SERVER_ERROR <br />
1 1715744138012;BAD_REQUEST;15.22 <br />
1 1715744138013;INTERNAL_SERVER_ERROR;23.72 <br />
3 BEFORE 1715744138011 <br />
3 AFTER 1715744138010 <br />
2 BAD_REQUEST <br />
4 BEFORE INTERNAL_SERVER_ERROR 1715744138011 <br />
4 AFTER INTERNAL_SERVER_ERROR 1715744138010 <br />


**Sample Output (output.txt):**

No output <br />
No output <br />
Min: 10.170000, Max: 23.720000, Mean: 16.945000 <br />
No output <br />
No output <br />
Min: 0.000000, Max: 0.000000, Mean: 0.000000 <br />
Min: 10.170000, Max: 23.720000, Mean: 18.207500 <br />
Min: 15.220000, Max: 15.220000, Mean: 15.220000 <br />
Min: 0.000000, Max: 0.000000, Mean: 0.000000 <br />
Min: 10.170000, Max: 23.720000, Mean: 19.203333 <br />


Author:
**Maharnab Ghosh**
