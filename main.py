from classes.Process import Process
import time

if __name__ == "__main__": 
    start_runtime = time.time()

    quantum1 = 0.001 # 1 milissegundos
    quantum2 = 0.01 # 10 milissegundos
    quantum3 = 0.1 # 100 milissegundos
    quantum4 = 1 # 1 segundo
    
    process_1_value = [0, 1, 0]
    process_2_value = [0, 1, 0]
    process_3_value = [0, 1, 0]
     
    process_1 = Process(1, 2, 100000)
    process_2 = Process(2, 3, 100000)
    process_3 = Process(3, 5, 100000)

    while (process_1_value[0] <= 100000) and (process_2_value[0] <= 100000) and (process_3_value[0] <= 100000):
        process_1_value = process_1.execute_process(quantum2, process_1_value[0], process_1_value[1])
        process_2_value = process_2.execute_process(quantum2, process_2_value[0], process_2_value[1])
        process_3_value = process_3.execute_process(quantum2, process_3_value[0], process_3_value[1])

    duration_execution = time.time() - start_runtime
    
    print(f'\nTempo do processo 1: {process_1_value[2]}')
    print(f'Tempo do processo 2: {process_2_value[2]}')
    print(f'Tempo do processo 3: {process_3_value[2]}')
    print(f'\nTempo Final: {round(duration_execution, 2)} segundos')