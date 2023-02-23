#Write a program that allows the user to enter five numbers (read as strings). Create a string that consists of the user’s numbers separated by plus signs. For instance, if the user enters 2, 5, 11, 33, and 55, then the string should be ‘2+5+11+33+55’.

num=int(input("Enter 5 numbers: "))
for i in str(num):
    new_str='+'.join(str(num))
print("New string is: ",new_str)


#Write a program that gets a string from the user containing a potential telephone number. The program should print Valid if it decides the phone number is a real phone number, and Invalid otherwise. A phone number is considered valid as long as it is written in the form abc-def-hijk or 1-abc-def-hijk. The dashes must be included, the phone number should contain only numbers and dashes, and the number of digits in each group must be correct. Test your program with the output shown below.
#Enter a phone number: 1-301-447-5820
#Valid
#Enter a phone number: 301-447-5820
#Valid
#Enter a phone number: 301-4477-5820
#Invalid
#Enter a phone number: 3X1-447-5820
#Invalid
#Enter a phone number: 3014475820
#Invalid

num = input("Enter the phone number: ")
if len(num) == 12 and num[3]==num[7]=="-" and (num[:3]+num[4:7]+num[8:]).isdigit():
    print("Valid")
elif len(num) == 14 and num[0]=="1" and num[1]==num[5]==num[9]=="-" and (num[2:5]+num[6:9]+num[10:]).isdigit():
            print("Valid")        
else:
    print("Invalid")


#Write a program that implements the Caesar cipher, a simple encryption technique where each letter in the plaintext is shifted a certain number of places down the alphabet (https://en.wikipedia.org/wiki/Caesar_cipher).

ls  = input("Enter the text: ")
k = int(input("Enter key: "))
def Ceaser_cipher(text, key):
    res=[]
    n=""
    a="abcdefghijklmnopqrstuvwxyz"
    a1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(text)):
        if text[i] in a:
            n=a
        elif text[i] in a1:
            n=a1
        else:
            res.append(text[i])
        
        if text[i] in n:
            for j in range(len(n)):
                if 0<=(j - key)<len(n) and text[i]==n[j]:
                    res.append(n[j-key])
                elif j-key<0 and text[i] == n[j]:
                    res.append(n[(j - key)%len(n)])
                        
    return ''.join(res)
print(Ceaser_cipher(ls, k))


#Write a program that calculates the Fibonacci sequence. The Fibonacci sequence is a series of numbers where each number is the sum of the two numbers preceding it. The first two numbers are 0 and 1, and the sequence goes 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on.
def Fibonacci(n):  
   if n <= 1:  
       return n  
   else:  
       return(Fibonacci(n-1) + Fibonacci(n-2))  
length = int(input("Enter the length:  ")) 
  
if length <= 0: 
   print("Please enter a positive integer")  
else:  
   print("Fibonacci sequence is: ")  
   for i in range(length):  
       print(Fibonacci(i), end=" ")


#Write a program that accepts a string from the user and removes all duplicates. The resulting string should contain only unique characters.
#1.
string =input('Enter a string: ')   
my_string = []
res=””
for i in string:
    if i not in my_string :
        my_string .append(i)
        res=" ".join(my_string)
print("New string is: ",res)  
#2.

string = input('Enter a string: ')
my_string = " "
for i in string:
    if i not in my_string:
        my_string += i
print("New string is: ",my_string)
