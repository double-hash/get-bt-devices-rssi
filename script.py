  GNU nano 3.2                                               test2.py                                                        

import subprocess
import shlex

devices = {}

# parse each lines
def parse_output(output):
        # split output line
        words = output.split()
        # print(words)
        # check if RSSI is present
        if len(words) == 5 and words[3] == "RSSI:":
                i = words.index("RSSI:")
                if i:
                        # cleaning the RSSI value and storing as an int value
                        s = words[4].replace('-','')
                        # words[2] is always MAC addr
                        devices[words[2]] = words[4]

def run_command(command):
        process = subprocess.Popen(shlex.split(command), shell=True, stdout=subprocess.PIPE)
        while True:
                output = process.stdout.readline()
                if process.poll() is not None:
                        break
                if output:
                        #print(output)
                        parse_output(output)
                        print(devices)
        rc = process.poll()
        return rc

run_command('bluetoothctl scan on')
#if the command doesn't start automatically, just type 'scan on' after launching the python script






