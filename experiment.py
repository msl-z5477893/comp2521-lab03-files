import subprocess
import sys

genType = ['R', 'A', 'D']

def cmd(genFlag, size):
    return ['./gen', size, flag, '|', '/usr/bin/time', '-f']

print('inputSize,timeSorted,timeRandom,timeReverseSorted')
for inputSize in range(10000, 101000, 1000):
    timeSorted = 0.0
    timeRandom = 0.0
    timeReverseSorted = 0.0
    for gt in genType:
        for _ in range(5):
            r = subprocess.run(['./timeUnitSort', f'{inputSize}', gt, sys.argv[1]], 
                               capture_output=True, text=True)
            # `time` command outputs to stderr, hence the command
            execTime = float(r.stderr)
            match gt:
                case 'R':
                    timeRandom += execTime
                case 'A':
                    timeSorted += execTime
                case 'D':
                    timeReverseSorted += execTime
        match gt:
            case 'R':
                timeRandom /= 5
            case 'A':
                timeSorted /= 5
            case 'D':
                timeReverseSorted /= 5
    timeSorted = round(timeSorted, 2)
    timeRandom = round(timeRandom, 2)
    timeReverseSorted = round(timeReverseSorted, 2)
    print(f'{inputSize},{timeSorted},{timeRandom},{timeReverseSorted}')


