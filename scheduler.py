import subprocess
import os
# Get the home directory in a cross-platform way
home_dir = os.path.expanduser("~")
#update dependancies
subprocess.call(["python3", f"{home_dir}/Window_Display/dependancies.py"])

from daemonize import Daemonize
import time
import schedule

def run_script():
    # Create a detached process running the script
    subprocess.Popen(["python3", f"{home_dir}/Window_Display/update_git.py"])

# Create a daemon
daemon = Daemonize(app="update_git", pid="/tmp/update_git.pid", action=run_script)

# Start the daemon
daemon.start()

