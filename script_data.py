import subprocess
import time

while True:
    subprocess.call(['./cronjob_node.sh'])
    time.sleep(3600)
