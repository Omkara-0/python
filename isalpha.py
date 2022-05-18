# Python code for implementation of isalpha() 
# checking for alphabets 
string = 'Ayush'
print(string.isalpha())

string = 'Ayush0212'
print(string.isalpha()) 
   
# checking if space is an alphabet
string = 'Ayush Saxena'
print( string.isalpha())

# Python program to illustrate 
# counting number of alphabets  
# using isalpha() 

string='Ayush Saxena'
count=0

# Initialising new strings 
newstring1 ="" 
newstring2 ="" 

# Iterating the string and checking for alphabets 
# Incrementing the counter if an alphabet is found 
# Finally printing the count 

for a in string: 
    if (a.isalpha()) == True: 
        count+=1
        newstring1+=a 

print(count) 
print(newstring1) 

string='Ayush0212'
count=0
for a in string: 
    if (a.isalpha()) == True: 
        count+=1
        newstring2+=a 

print(count) 
print(newstring2)
