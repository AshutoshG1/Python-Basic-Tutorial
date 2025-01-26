#Loops 
# while True:
#     print("Hello")

# count = 1;
# while count<=5:
#     print("Hello")
#     count += 1
# print(count)

# i = 1
# while i<=5:
#     print("python")
#     i = i+1

# i = 5
# while i>=1:
#     print("Hello")
#     i -= 1
# print(i)

# #print numbers from 1 to 100
# i = 1
# while i<=100:
#     print(i)
#     i += 1

# # print numbers from 100 to 1
# i = 100
# while i>=1:
#     print(i)
#     i -= 1

# # print the multiplication table of number of n
# n = int(input("Enter the number : "))
# i = 1
# while i<=10:
#     print(i*n)
#     i += 1

# #print the element of the following list using a loop [1,4,9,16,25,36,49,64,81,100]
# list = []
# i = 1
# while i<=10:
#     list.append(i*i)
#     i = i+1
# print(list)

# #Search for a number x in a list [1,4,9,16,25,36,49,64,81,100]
# nums = [1,4,9,16,25,36,49,64,81,100]
# element = int(input("Enter the number : "))
# i = 0
# while i < len(nums):
#     if element == nums[i]:
#         print("element is present at index ",i)
#         break
#     i +=1

# #break statement
# i = 1
# while i <= 5:
#     print(i)
#     if(i==3):
#         break
#     i += 1

# #continue statement
# i = 1
# while i <= 5:    
#     if(i==3):
#         i = i + 1
#         continue
#     print(i)
#     i += 1

# #For Loops 
# nums = [1,2,3,4,5]

# for val in nums:
#     print(val)

# tup = (1,2,3,4,5)
# for val in tup:
#     print(val)

# str = "Techie Ashutosh"

# for ch in str:
#     if(ch=='o'):
#         print(" o found ")
#         break
#     print(ch)
# else:
#     print("End")

# nums = [1,4,25,36,49,64,81,100]
# for val in nums:
#     print(val)

# nums = [1,4,25,36,49,64,81,100]
# x = 36
# for val in nums:
#     if(x==val):
#         print("found")


# for val in range(5):
#     print(val)

# for val in range(1,5):
#     print(val)

# for val in range(1,10,2): #(start,end,step-size)
#     print(val)

# #print numbers from 1 to 100
# for val in range(1,101):
#     print(val)

# #print numbers from 100 to 1
# for val in range(100,0,-1):
#     print(val)

# #multiplication table of a number 
# n = int(input("Enter a number : "))
# for val in range(1,11):
#     print(n*val)

# for i in range(5):
#     pass
# print("some useful task")

# i=1
# if(i>5):
#     pass
# print("some task")

# #WAP to find the sum of first n natural numbers using while loop
# n = 5
# sum = 0
# for i in range(1,n+1):
#     sum += i
# print("Total sum = ",sum)

# #WAP to find the factorial of first n numbers using for loop
# n = 5
# fact = 1
# for i in range(1,n+1):
#     fact = fact*i
# print("Total factorial = ",fact)