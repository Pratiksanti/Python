# sum of even numbres 

print("sum of Even Numbers ")
n=int(input("Enter the n numbers :- "))
total_sum=0
for i in range(1,n+1):
   if i%2==0:
     print(i)
     total_sum+=i
print("The sum of Even numbers is :- ")
print(total_sum)


# sum of Even Numbers 
# Enter the n numbers :- 10
# 2
# 4
# 6
# 8
# 10
# The sum of Even numbers is :-
# 30