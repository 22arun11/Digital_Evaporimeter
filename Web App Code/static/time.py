import time
import subprocess

while True:
    subprocess.call(["python", "dynamo.py"])
    time.sleep(5)