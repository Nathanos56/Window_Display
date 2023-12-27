import git
import os

# # Navigate to the directory
# os.chdir(f'/home/{os.getlogin()}/Window_Display')

# Get the home directory in a cross-platform way
home_dir = os.path.expanduser("~")

# Construct the path to the directory
dir_path = os.path.join(home_dir, 'Window_Display')

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

print("Suck that")
print("it worked")
