# single-line code

'''
multiline line comment
hhfhh
fffjhg
'''
# Here to print hello world
#print('hello,world')
# creating a variable
''' python is a dynamically typed language
python is case sensitive
'''
a = 10
b= 20
c=a+b
name="python"
num1='10'
num2='20'
add=num1+num2
name='siva'
num=10.01000
#print(type(num))
''' rules for naming a variable in python 
1. variable name should not start with a number example: 1name
2.no special characters are allowed except underscore(_) example: __init__ (allowed) @name (not allowed)
3.Name -  name are not same as Name 
4. name should not be a keyword example : if,else,elif,string,int,float
'''

# control flow statements
# voting age check
''' 
age=int(input('Enter ur age:') )# input values are always in sting datatype

if (age==18):
    print('u r eligible for voting')
elif (age>18):
    print('u r eligible for voting')
else:
    remaining=18-age
    print('u r not eligible for voting,still you have to wait for',remaining,'years')       
'''
# string formatting
name='sivaraman'
age=21
#print(name + age) #error str and int cannot be added 
print(f'my name is {name} and my age is {age}')  

