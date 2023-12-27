import subprocess
import os

def run_script(script_path):
    # Create a detached process running the script
    subprocess.Popen(["python", script_path])

# Call the function with the path to your script
run_script("update_git.py")
