n = int(input("Enter the total process number: "))
process= []
burstTime=[]
priority=[]
waitTime =[0]*n
TAT= [0]*n

for i in range(n):
    process.append(i)

    bt=int(input(f"Enter burst time for P{i+1} :"))
    burstTime.append(bt)

    pr= int (input(f"Enter priority for P{i+1} :"))
    priority.append(pr)

for i in range(n):
    for j in range(i+1,n):
        if priority[i]<priority[j]: #high number = high priority 
        #if priority[i] > priority[j]: ( low = high priority)    
            priority[i],priority[j]= priority[j],priority[i]
            burstTime[i],burstTime[j]=burstTime[j],burstTime[i]
            process[i],process[j]=process[j],process[i]

for i in range (1,n):
    waitTime[i]= waitTime[i-1]+ burstTime[i-1]

for i in range(n):
    TAT[i]= waitTime[i] + burstTime[i]

print( "\nprocess\tpriority\tburst\tTAT\twaiting time")
for i in range(n):
    print( f"{process[i]}\t{priority[i]}\t\t{burstTime[i]}\t{TAT[i]}\t{waitTime[i]}")