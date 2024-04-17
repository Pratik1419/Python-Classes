# st = "Print only the words that start with s in this sentence"

# for word in st.split():
#     if word[0] == "s":
#         print(word)

# for i in range(0,11,2):
#     print(i)

# mylist = [i for i in range(1,51) if(i%3 == 0)]
# print(mylist)

# st = "Print every word in this sentence that has an even number of letters"
# for string in st.split():
#     if len(string)% 2 == 0:
#         print(string+ "<-- ha a even length!")


# for i in range(0,101):
#     if (i % 3 == 0 and  i % 5 == 0):
#         print("FizzBuzz", i)
#     elif (i % 3 == 0):
#         print("Fizz", i)
#     elif (i % 5 == 0):
#         print("Buzz", i)
# else:
#         print("The end of this part")

# st = "Create a list of the first letters of every word in this string"
# word = [sts[0] for sts  in st.split()]
# print(word)

# def say_hello(name):
#     print(f'Hello {name}')

# say_hello("pratik")

# num = [1,2,3,4,5,6,7,8,9,10]

# for number in num:
#     if number % 2 == 0:
#         return True
#     else:
#         pass


num_list = [1,2,3,4,5,6]

def check_even_list(num_list):

    for number in  num_list:
        if number % 2 == 0:
            return True
        else:
            pass
    return False
