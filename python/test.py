import os

current_dir = os.curdir
project_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
output_dir = os.path.join(project_dir, 'output')
latex_dir = os.path.join(project_dir, 'SampleResumeTemplate')

print("Current working directory before change:", os.getcwd())  # Print current working directory
os.chdir(latex_dir)
print("Current working directory after change:", os.getcwd())  # Print current working directory after change
