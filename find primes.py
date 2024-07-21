
import math, time


def prime_seive(limit):
    global end, start
    
    limit+=1
    nums = [True] * (limit)
    nums[0] = nums[1] = False
    
    start = time.perf_counter()
    for i in range (2, int(math.sqrt(limit))):
        if nums[i] == True:
            for j in range( i*i , limit, i):
                nums[j] = False
    end = time.perf_counter()
    return nums
    
limit = int(input("Find all primes up to: "))

end=0
start=0

primes=prime_seive(limit)

total_time = end-start
count = 0
for x in range(len(primes)):
    if primes[x] == True:
        count +=1
        #print (count,":",x)
print (total_time)

print("I found", count,"prime numbers.")
ans=input("Do you want me to print them out?")
ans=ans.lower()
ans=ans.strip()
print (ans)

if ans !="y" and ans!="yes":
    print("Thanks for playing!  Goodbye!")
    exit()

count = 0
for num in range(0, limit):
    if primes[num] == True:
        count += 1
        print (count,":",num," is prime.")
                
