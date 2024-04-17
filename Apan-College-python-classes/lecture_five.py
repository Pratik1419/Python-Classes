# About loops
# count = 1
# while count <= 5:
#     print("hello")
#     count += 1

    # print(count)

# i = 100
# while i >= 1:
#     print(i)
#     i-= 1

# n = 1
# while n<=10:
#     print(8*n)
#     n +=1

# list = [1,4,9,16,25,36,49,64,81,100]
# idx = 0

# while  idx < len(list):
#     print(list[idx])
#     idx+=1

# num = (1,4,9,16,25,36,49,64,81,100)

# x = 25

# i = 0
# while i < len(num):
#     if(num[i] == x):
#         print("FOUND at idx", i)
#         break
#     else:
#         print("Finding....")
#     i += 1

# print("end of loop")

# questions
# num = [1,4,9,16,25,36,49,64,81,100]
# for val in num:
#     print(val)
# else:
#     print("end")

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# usernum = int(input("Enter a number : "))

# idx = 0
# for val in nums:
#     if(val == usernum):
#         print("Number found at idx", idx)
#     idx += 1

# for i in range(2,10,2):  
#     print(i)


# question A
# for i in range(1, 101):
#     print(i)

# question B
# for i in range(100, 0, -1):
#     print(i)

# question C
# n = int(input("Find the multpliction table of:"))

# for i in range(1, 11):
#     print(n*i)

# n = int(input("Enter a number to find the sum of nth num:"))
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print("total sum =",sum)


n = 5

fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial is ", fact)