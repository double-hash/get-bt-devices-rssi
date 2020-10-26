import subprocess
import shlex

devices = {}

# parse each lines
def parse_output(output):
          # split output line
          words = output.split()
          # check if RSSI is present
          if len(words) == 6 and words[4] == "RSSI:":
                 # words[3] is always MAC addr
		 # sorting MAC addr as key and RSSI as value in devices
                 devices[words[3]] = words[5]

def run_command(command):
    #opening process
    process = subprocess.Popen(shlex.split(command), shell=True, stdout=sub$
    #looping for getting new values
    while True:
         output = process.stdout.readline()
         if process.poll() is not None:
             break
         if output:
	     #formatting output and storing in devices
             parse_output(output)
             #print output stored in devices
             print devices
    rc = process.poll()
    return rc

run_command('bluetoothctl scan on')
