import subprocess
from path_config import *

def run_subprocess(command, quiet=False, dry=False):
    """Run shell-command."""
    print("[{}]----------".format("RUN"))
    print(command)
    
    if dry:
        return
    
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if quiet == False:
        print("[{}]--------".format("ERROR"))
        print(stderr.decode())
        print("[{}]-------".format("OUTPUT"))
        print(stdout.decode())
    
    return stdout.decode(), stderr.decode()
