# Exercises for chapter 3:

# Name: Olha Vasylevska


# Exercise 3.1

# If you try to call a function before it is defined, it will result in error: NameError: name 'repeat_lyrics' is not defined



# Exercise 3.2

# It will work just fine. No error messages.



# Exercise 3.3

# The string s will be printed starting from the (70-len(s)+1) position and the last letter of the string will be in the position 70. 
# Assuming 70th column is counted from 0, as characters in python string start from 0.

def right_justify(s):
    print " "*(70 -(len(s)-1)) + s

right_justify('allen')



# Exercise 3.4

#1.  
def do_twice(f):
	f()
	f()
    
def print_spam():
    print 'spam'
    
do_twice(print_spam)

# Result: spam
#         spam    

#2.  
def do_twice(f, a):
	f(a)
	f(a)

#3.  
def print_twice(s):
    print s
    print s

#4.
do_twice(print_twice, 'spam')

#5.
def do_four(f, value):
	do_twice(value)
	do_twice(value)




