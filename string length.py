s='python'
index_last_char=len(s)-2
print(index_last_char)
print (index_last_char-1)
#the function len() counts the no of characters in a string
#in python indices are numbered from right to left which makes it 
#easy to access the last character of a given string for example:

#The name FANTASTIC has its strings numbered accordingly
#F=-1
#A=-2
#N=-3
#T=-4
#A=-5
#S=-6
#T=-7
#I=-8
#C=-9

S='FANTASTIC'
first_char=S[-1]
print (first_char)

#strings also can be concantenated i.e you can add them to each other 

b= '*'+'*'
print (b)

#You cut a "slice" out of a string. In the following expression, [2: 4]
#means that we cut out a substring from the string "Python", which
#begins with the character of index 2 (inclusive) and goes up to index
#4 (exclusive):
m="Python" [2: 4 ]
print (m)