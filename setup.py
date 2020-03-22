from subprocess import run

run(['sudo', 'ln', 'main.py', '/usr/bin/run'])
print('symbolic link created in /usr/bin/run')

