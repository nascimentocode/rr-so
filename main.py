from classes.Process import Process
import time

def runAllProcess(quantum):
    startRuntime = time.time()

    processValue1 = [0, 1, 0]
    processValue2 = [0, 1, 0]
    processValue3 = [0, 1, 0]

    process1 = Process(1, 2, 100000)
    process2 = Process(2, 3, 100000)
    process3 = Process(3, 5, 100000)
    
    tempProcessTime1 = []
    tempProcessTime2 = []
    tempProcessTime3 = []

    while (processValue1[0] <= 100000) and (processValue2[0] <= 100000) and (processValue3[0] <= 100000):
        processValue1 = process1.execute_process(quantum, processValue1[0], processValue1[1])
        tempProcessTime1.append(processValue1[2])
        processValue2 = process2.execute_process(quantum, processValue2[0], processValue2[1])
        tempProcessTime2.append(processValue2[2])
        processValue3 = process3.execute_process(quantum, processValue3[0], processValue3[1])
        tempProcessTime3.append(processValue3[2])

    runtime = time.time() - startRuntime
    
    processTime1 = findTimeProcess(tempProcessTime1)
    processTime2 = findTimeProcess(tempProcessTime2)
    processTime3 = findTimeProcess(tempProcessTime3)

    return [round(runtime, 2), processTime1, processTime2, processTime3]
    
def findTimeProcess(list):
    counter = 0
    for time in list:
        counter+=time
    
    return round(counter, 2)

if __name__ == "__main__": 
    quantums = [0.001, 0.01, 0.1, 1]

    timesQuantum1 = []
    timesQuantum2 = []
    timesQuantum3 = []
    timesQuantum4 = []

    for quantum in quantums:
        timesQuantum = runAllProcess(quantum)
        if quantum == 0.001:
            timesQuantum1.append(timesQuantum[0])
            timesQuantum1.append(timesQuantum[1])
            timesQuantum1.append(timesQuantum[2])
            timesQuantum1.append(timesQuantum[3])
        elif quantum == 0.01:
            timesQuantum2.append(timesQuantum[0])
            timesQuantum2.append(timesQuantum[1])
            timesQuantum2.append(timesQuantum[2])
            timesQuantum2.append(timesQuantum[3])
        elif quantum == 0.1:
            timesQuantum3.append(timesQuantum[0])
            timesQuantum3.append(timesQuantum[1])
            timesQuantum3.append(timesQuantum[2])
            timesQuantum3.append(timesQuantum[3])
        elif quantum == 1:
            timesQuantum4.append(timesQuantum[0])
            timesQuantum4.append(timesQuantum[1])
            timesQuantum4.append(timesQuantum[2])
            timesQuantum4.append(timesQuantum[3])

    print('\nQuantum 1 = 1 Milissegundos')
    print(f'\nTempo do processo 1: {timesQuantum1[1]}')
    print(f'Tempo do processo 2: {timesQuantum1[2]}')
    print(f'Tempo do processo 3: {timesQuantum1[3]}')
    print(f'Tempo Final: {timesQuantum1[0]} segundos')

    print('\nQuantum 2 = 10 Milissegundos')
    print(f'\nTempo do processo 1: {timesQuantum2[1]}')
    print(f'Tempo do processo 2: {timesQuantum2[2]}')
    print(f'Tempo do processo 3: {timesQuantum2[3]}')
    print(f'Tempo Final: {timesQuantum2[0]} segundos')

    print('\nQuantum 3 = 100 Milissegundos')
    print(f'\nTempo do processo 1: {timesQuantum3[1]}')
    print(f'Tempo do processo 2: {timesQuantum3[2]}')
    print(f'Tempo do processo 3: {timesQuantum3[3]}')
    print(f'Tempo Final: {timesQuantum3[0]} segundos')

    print('\nQuantum 4 = 1 Segundo')
    print(f'\nTempo do processo 1: {timesQuantum4[1]}')
    print(f'Tempo do processo 2: {timesQuantum4[2]}')
    print(f'Tempo do processo 3: {timesQuantum4[3]}')
    print(f'Tempo Final: {timesQuantum4[0]} segundos')