import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# List of dependencies
dependencies = ['PIL', 'tkinter', 'schedule']  # Add your dependencies here    'GitPython',

# Try to import the dependencies
for dependency in dependencies:
    try:
        __import__(dependency)
        print(f"{dependency} is installed.")
    except ImportError:
        print(f"{dependency} is not installed. Installing...")
        install(dependency)
