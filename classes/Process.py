import time

class Process:
    def __init__(self, id, base, expoent):
        self.id = id
        self.base = base
        self.expoent = expoent

    def execute_process(self, quantum, i, potency):
        startProcessTime = time.time() #Pega a hora que comecou/Inicio do tempo do processo
        
        while (time.time() - startProcessTime < quantum) and (i <= self.expoent):
            potency*=self.base
            print(f"Processo {self.id}: {i}")
            i+=1
        
        endProcessTime = time.time() #Pega a hora que acabou/Fim do tempo do processo
        processTime = endProcessTime - startProcessTime #Subtrai para saber quanto tempo durou o processo

        return [i, potency, processTime]