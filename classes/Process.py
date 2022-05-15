import time

class Process:
    def __init__(self, id, base, expoent):
        self.id = id
        self.base = base
        self.expoent = expoent

    def execute_process(self, quantum, i, potency):
        start_process_time = time.time() #Pega a hora que comecou/Inicio do tempo do processo
        
        while (time.time() - start_process_time < quantum) and (i <= self.expoent):
            potency*=self.base
            print(f"Processo {self.id}: {i}")
            i+=1
        
        end_process_time = time.time() #Pega a hora que acabou/Fim do tempo do processo
        process_duration = end_process_time - start_process_time #Subtrai para saber quanto tempo durou o processo

        return [i, potency, round(process_duration, 2)]