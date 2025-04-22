# sum of odd numbers 
print("sum of odd Numbers ")
n=int(input("Enter the n numbers :- "))
total_sum=0
for i in range(1,n+1):
   if i%2==0:
     print()
   else:
      print(i)
      total_sum+=i
print("The sum of odd numbers is :- ")
print(total_sum)


# sum of odd Numbers 
# Enter the n numbers :- 10
# 1

# 3

# 5

# 7

# 9

# The sum of odd numbers is :-
25