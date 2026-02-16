#SJF
n = int(input("Enter the process number: "))
process = []
Bt=[]
Wt=[0]*n
tat=[0]*n

for i in range (n):
    process.append(f"P{i+1}")
    a=int(input(f"Enter burst time for {process[i]}: "))
    Bt.append(a)    

for i in range(n):
    for j in range(i+1,n):
        if Bt[j]<Bt[i]:
            Bt[i],Bt[j]=Bt[j],Bt[i]
            process[i],process[j]=process[j],process[i]

for i in range (1,n):
    Wt[i]=Wt[i-1]+Bt[i-1]
    tat[i]= Wt[i]+Bt[i]

print("\nProcess\tBurst\tWt\tTAT")
for i in range(n):
    print(process[i],"\t",Bt[i],"\t",Wt[i],"\t",tat[i])

