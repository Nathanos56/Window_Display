import subprocess
#update dependancies
subprocess.call(["python3", "dependancies.py"])

import os
from daemonize import Daemonize
import time
import schedule

def run_script():
    # Create a detached process running the script
    subprocess.Popen(["python3", "update_git.py"])

# Create a daemon
daemon = Daemonize(app="update_git", pid="/tmp/update_git.pid", action=run_script)

# Start the daemon
daemon.start()

