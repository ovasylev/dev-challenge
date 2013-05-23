# Exercises for chapter 2:

# Name: Olha Vasylevska

# Exercise 2.1

# If a number starts from 0, Python interpreter considers it to be in octal numeral system (base 8), which uses the digits from 0 to 7.
# Since 02492 contains 9, which doesn't exist in this system, it results in error.
# 02132 is octal number of integer 1114.
# Accordingly: 01 --> 1; 010 --> 8; 0100 --> 64; 01000 --> 512;



# Exercise 2.2

# If you create a script with the following statesments:

# 5
# x = 5 
# x + 1

# and run it, than nothing will be displayed on the screen.
# You have to change it the following way

# print 5
# x = 5
# print x + 1

# so when you run the script again, it will result in the following:

# 5
# 6



# Exercise 2.3

# width = 17
# height = 12.0
# delimiter = '.'

# width/2 = 8             Integer
# width/2.0 = 8.5         Float
# height/3 = 4.0          Float
# 1 + 2 * 5 = 11          Integer
# delimiter*5 = '.....'   String



# Exercises 2.4

#1. from math import print pi 
#   4.0 / 3 * pi * 5 ** 3 = 523.5987755982989

#2. (1*3.0) + (59*0.75) + (60*24.95)*0.6 = 945.45

#3.  1*(8 +15.0/60) + 3*(7 + 12.0/60) + 1*(8 + 15.0/60) = 38.1 minute = 38m06s
#    6h52m + 38m06s = 7h30h06s = 07:30:06 am