import os
import sys
from datetime import datetime
import socket
import json

try:
    jsonSource = sys.argv[1]
except:
    sys.exit("Error: Missing arguments")

local_ip = socket.gethostbyname(socket.gethostname())
print("Local ip: " + local_ip)
start_time = datetime.now()
print("Current time: " + str(start_time))
print("Starting analysis...")

print('possible_json_string')
data = jsonSource.read()
js = json.loads(data.decode("utf-8"))
print(js)

end_time = datetime.now() - start_time
print("\aAnalysis completed.")