import subprocess
#update dependancies
subprocess.run(["python3", "dependancies.py"])

import git
import os
import time
import schedule

app_location = "Window_Display"

def Job():
    # Get the home directory in a cross-platform way
    home_dir = os.path.expanduser("~")

    # Construct the path to the directory
    dir_path = os.path.join(home_dir, app_location)

    # Navigate to the directory
    os.chdir(dir_path)

    # Initialize a Git object
    repo = git.Repo('.')

    # Fetch the latest changes from the main branch
    repo.remotes.origin.fetch('main')

    # Get the commit hash of the local and remote main branch
    local_commit = repo.heads.main.commit.hexsha
    remote_commit = repo.remotes.origin.refs.main.commit.hexsha

    # If the commit hashes are not the same, pull the latest changes
    if local_commit != remote_commit:
        repo.remotes.origin.pull('main')
    
    print("I did a job")
    


#checks github every 5 minutes
schedule.every(5).minutes.do(Job)
    
# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)

#print("Suck that")
#print("it worked")
