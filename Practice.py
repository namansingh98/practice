# #list are mutable  we can add update
# # order indexing and slcing are allowed 
# #heterogeneous data type

# from operator import index


# l = [1,2,3,4,5,"a","b","c","d", 10, 20, 30, 40,]
# # print(l,type(l))


# #indexing and sliciing
# print(l[-1])

# print(l[2:-5])


# # # # Operators in Python 1 Arithmetic operators +,-,*,/,//1%," 
# 2 Comparison operators <I>,<=1>=,==,!= 
# num1 = 10 # num2 =20 # print(numl + num2) # print(numl - num2) # print(numl * num2) # print(10/3) # print(10//3) # print(10%3) 
# print(45 ** 6) 

# # statements # elif [condition]: # statemnts # else: # statements 
# num1 = 100 
# num2 = 500 
# # 1 numi is greater # 2 num2 is greater # 3 numi and num2 are equal 
# if num1 > num2: 
#     print("num1 is greater than num2") 
# elif num2 >num1: 
#     print("num2 is greater than num1") 
# else: 
#     print("num1 and Num2 are equal") 


# a_list = [1, 2, 3, 4,5,6,7,8,9,10,11,12]
import math

num = 66.532 print(math.modf(num))   
d, i + math.modf(num) print (i)
# even = []
# odd = []
# for item in a_list:
#   if item % 2 == 0:
#     even.append(item)
#   else:
#     odd.append(item)

# print(even,odd)


#  SHORT HANDED

# list=[1,2,3,4,5,6,7,8]
# even= [item for item in list if % 2=0]
# odd =[item for item in list if % 3=0]

# print(odd,even)

# ODD EVEN ||


# for i in range(1500,2700):
#     if i%5==0 and i%7==0:             in this if condition py will devide the value from 5 and 7 when the value % i =0 value should be 0
#      print(" ",i)



# finding the value find those number which are divide by 7 and 5 between 1500 and 2700
 
# write the value when value devide with 3 and 5 then print fizz , buzz

# for fizzbuzz in range(51):
#     if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
#         print("fizzbuzz")
#         continue
#     elif fizzbuzz % 3 == 0:
#         print("fizz")
#         continue
#     elif fizzbuzz % 5 == 0:
#         print("buzz")
#         continue
#     print(fizzbuzz)


# a_list = [1, 2, 3, 4,5,6,7,8,9,10,11,12]
# even = []
# odd = []
# for item in a_list:
#   if item % 2 == 0:
#     even.append(item)
#   else:
#     odd.append(item)
#
# print(even,odd)

#
#  SHORT HANDED

# list=[1,2,3,4,5,6,7,8]
# even= [item for item in list if % 2=0]
# odd =[item for item in list if % 3=0]
#
# print(odd,even)

# ODD EVEN ||

#
# for i in range(1500,2700):
#     if i%5==0 and i%7==0:             in this if condition py will devide the value from 5 and 7 when the value % i =0 value should be 0
#      print(" ",i)


# finding the value find those number which are divide by 7 and 5 between 1500 and 2700

# write the value when value devide with 3 and 5 then print fizz , buzz
#
# num = 33.332
# print(round(num,3))
# #
# import math
# # l= [0.6]*5# print(l)
# # print(sum(l))
# # 5 6
# num=5.444
# print(math.floor(4),math.ceil(4))

#
# for fizzbuzz in range(51):
#     if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
#         # when the value devide with 5 and 3 then it will print fizzbuzz
#         print("fizzbuzz")
#         continue
#     elif fizzbuzz % 3 == 0:
#         print("fizz")
#         continue
#     elif fizzbuzz % 5 == 0:
#         print("buzz")
#         continue
#     print(fizzbuzz)


import math
#
# num = 66.532
# print(math.modf(num))
#
# d, i = math.modf(num)
# print (i)
#
# l= [1,2,3,4,5,6]
# print(random.choice(l))

#
# import random
# print(random.randint(1,80))
# uniform give you floating point point number
# # randrange doesnot give the end value but randint its opposite
# print(random.randrange(1,80))


# user define function
# we can call any function with defenation  or function call
# when we try to get the value from backwards then we have to put value form -1

# append(method) is not effect the list or value it only insert into the origial list


def value_reverse(value):
    reverse=value[::-1]
    return reverse
l="python"
result=value_reverse(l)
print(result)

