import subprocess, time
from threading import Thread
import csv, pandas as pd

#cpu temp before; cpu temp during; cpu temp after, elapsed time; power usage before; power usage during; power usage after

def getCPUTemp() -> list:
    return float(subprocess.check_output(['bash', 'cat /sys/class/thermal/thermal_zone*/temp']))/1000

def runTest(type: str):
    subprocess.check_output(['bash', f'{type}/run.sh'])

def runTests(type: str, csvwriter):
    info = {
        'CPUTempBefore': None,
        'CPUTempDuring': None, 
        'CPUTempAfter': None,
        'ElapsedTime': None,
    }

    for i in range(numOfTests):
        thread = Thread(target = runTest, args = (type))
        startTime = time.Time()
        
        #before
        info['CPUTempBefore'] = getCPUTemp()
        
        thread.start()
        time.sleep(6)

        #~mid test
        info['CPUTempDuring'] = getCPUTemp()
        info['PowerDuring'] =  getPower()
        
        thread.join()
        time.sleep(5)

        #after
        info['CPUTempAfter'] = getCPUTemp()
        info['ElapsedTime'] = time.Time() - startTime
        
        csvwriter.writerow([info['CPUTempBefore'], info['CPUTempDuring'], info['CPUTempAfter'], info['ElapsedTime']])

        #let the cpu cool down
        time.sleep(60)

if __name__ == '__main__':
    numOfTests = 100

    with open("data.csv", "w", newline='') as f:
        csvwriter = csv.writer(f)

        #initial setup
        csvwriter.writerow(['CPU Temp Before (C)', 'CPU Temp During (C)', 'CPU Temp After (C)', 'Elapsed Time (s)', 'Power Usage Before (W)', 'Power Usage During (W)', 'Power Usage After (W)'])

        #Run C++ tests
        runTests('cpp', csvwriter)

        #Run Java tests
        runTests('java', csvwriter)

        #Run Python tests7
        runTests('python', csvwriter)