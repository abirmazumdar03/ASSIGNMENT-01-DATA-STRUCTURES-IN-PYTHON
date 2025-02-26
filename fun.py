import time
lst=[]
def fibo(i):
    if(i==1):
        lst.append(0)
    elif(i==2):
        lst.append(1)
    else:
        lst.append(lst[i-2-1]+lst[i-1-1])
n=int(input("Enter a Limit : "))

start_time=time.perf_counter()
for i in range(1,n+1):
    fibo(i)
end_time=time.perf_counter()
print("My Fibonnaci Series : ",lst)
print(f"Total Time by DP : {round((end_time-start_time),5)}")
