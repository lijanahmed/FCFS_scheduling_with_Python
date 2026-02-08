# First come first serve

process=[]
arivalTime = []
burstTime = []
completionTime= []
tat= []
waitingTime= []

proNum= int(input("Enter the process number: "))

def getInput():
    
    for i in range(proNum):
        procName= input(f"Enter process{i+1} name: ")
        process.append(procName)
        arTime= int(input(f"Arival Time for {process[i]}: "))
        arivalTime.append(arTime)
        brTime= int(input(f"Burst Time for {process[i]}: "))
        burstTime.append(brTime)

def calculate():
    comTime=0
    for i in range(proNum):
        comTime+= burstTime[i]
        completionTime.append(comTime)

        tat.append(completionTime[i]- arivalTime[i])
        waitingTime.append(tat[i]- burstTime[i])


def showResult():
    getInput()
    calculate()
    print("process   Arival Time   Burst Time   completion Time   TAT time   waiting Time ")
    for i in range(proNum):
        print(f"  {process[i]}           {arivalTime[i]}            {burstTime[i]}               {completionTime[i]}             {tat[i]}           {waitingTime[i]} ")


showResult()

