import os
import sys
from datetime import datetime
import re

try:
    source = sys.argv[1]
except:
    sys.exit("Error: Missing arguments")

print("\n")
start_time = datetime.now()
print("Current time: " + str(start_time))
print("\n")
print("Starting analysis...")
print("\n\n")

infile = open(source, 'r')
lines = infile.readlines()

for line in lines:
    # Qui bisogna usare le regex per fare i vari match
    if re.search("emmanuel", line):
        print(line.strip())

print("\n\n")
end_time = datetime.now() - start_time
print("Total time:" + str(end_time))
print("\n")
print("\aAnalysis completed.")