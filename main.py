#!/usr/bin/python3

from sys import argv
import subprocess
import os

arguments = argv
if '/usr/bin/run' in arguments:
    arguments.remove('/usr/bin/run')
file_to_run = arguments[0]

def python_runner(given_file, compiler='python3'):
    subprocess.run([compiler, given_file])

def cpp_runner(given_file, compiler='g++'):
    subprocess.run([compiler, given_file])
    subprocess.run(['./a.out'])
    subprocess.run(['rm', 'a.out'])

detectors = {
        'py': python_runner,
        'cpp': cpp_runner,
        }

file_extension = file_to_run.split('.')[-1]
if not file_extension in detectors.keys():
    print('Cannot find a runner for extension')
    exit()
runner = detectors[file_extension]
runner(file_to_run)

