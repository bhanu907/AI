def towerofhanoi(n,source,destination,auxiliary):
    if n==1:
        print("move disk 1 from source",source,"to destination",destination)
        return
    towerofhanoi(n-1,source,auxiliary,destination)
    print("move disk",n,"from source",source,"to destination",destination)
    towerofhanoi(n-1,auxiliary,destination,source)
n=3
towerofhanoi(n,'A','B','C')