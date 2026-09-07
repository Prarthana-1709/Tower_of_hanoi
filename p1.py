def tower_of_hanoi(n,auxilary,source,desitination):
    if n==1:
        print("move disk 1 from",source ,"to",desitination)
        return
    tower_of_hanoi(n-1,source,desitination,auxilary)
    print("move disk",n,"from",source ,"to",desitination)
    tower_of_hanoi(n-1,auxilary,source,desitination)
n=int(input("enter the number of disks"))
tower_of_hanoi(n,'A','B','C')
    
