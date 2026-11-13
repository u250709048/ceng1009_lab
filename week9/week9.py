# def is_odd(n):
#     return n % 2 == 1
#
#
#
#
#
# def is_leap_year(year):
#     if year%400==0:
#         return True
#     elif year%100==0:
#         return False
#     elif year%4==0:
#         return True




# def print_triangular_number(n):
#     sum=0
#     for i in range(1,n+1):
#         sum+=i
#         print(i,sum)
#
# print(print_triangular_number(5))




# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#
#     return True




# def reverse_string(s):
#     result =""
#     for ch in s:
#         result+=result
#     return result




# def remove_all(sub,s):
#     return s.replace(sub,"")
#
# print(remove_all("an","banana"))



# def substitute(message,key):
#     alphabet="abcçdefghijklmnoöpqrsştuüvyz"
#     result=""
#     for ch in message:
#         index=alphabet.find(ch.lower())
#         if index==-1:
#             result+=ch
#
#         elif ch.isupper():
#             result= result+key[index].upper()
#         else:
#             result= result+key[index].lower()
#
#     return result
#
# key= "qwertyuıopğüasdfghjklşizxc"
# print(len(key))
# print(substitute("hello world",key))




#
# def remove_dups(text):
#     result=""
#     for letter in text:
#         if letter not in result:
#             result+=letter
#
#         return result
#
# print(remove_dups("hello"))











