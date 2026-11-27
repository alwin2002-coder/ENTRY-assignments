# generator function for even numbers

def even_number(a,b):
    for i in range (a,b):
        if i % 2 == 0:
         yield i

a=even_number(2,10)
print(list(a))     


# decorator function

def main(x):
    def sub():
        print ("hello")
        x()
      
    return sub

@main
def xyz():
    print("my name is alwin")

xyz()


# regular expression
import re

x = "send your resume to my email, alwinwilson86@gmail.com or alwinwilson755@gmail.com."
y = "you can call me at at evening 7pm. my number is (123)4567890 or 0987654321. "

# to find emails
p=r'\b[a-z0-9]+@[a-z]+.[a-z]+\b'
email= re.findall(p,x)
print("email : ",email)

# to find phone numbers
p=r'\(\d{3}\)\d{7}|[0-9]{10}'
numbers=re.findall(p,y)
print("numbers =",numbers)


# to replace a word

p="7pm"
a=re.sub(p,"9pm",y)
print (a)