#python 3.7.1

#.format function
#.split function
#.append function

'''.remove function
use only value as a parameter
syntax : var_name.remove(value)'''

#.insert function
#.capitalize function
#.upper function
#.lower function
#.add function
#.discard function

'''.pop function
use also index as a parameter
.pop returns a deleted value
syntax : var_name.pop(index)'''

#.copy function
#.sort function
#.sorted function
#.count function
#.index function
#.tuple function

tuple = ("1", "2", "3", "4", "One", "Two", "Three", "Four")
set = {"1", "2", "3", "4", "One", "Two", "Three", "Four"}
std = str(input("Name : "))
reg = input("Reg.No : ")

print("\nName : " + std + "\nReg.No : " + str(reg))
print(f"\nName : {std} \nReg.No : {reg}")
print("\nName : {} \nReg.No : {}".format(std, reg))

#swap the values of variables
print("\nName : {1} \nReg.No : {0}".format(std, reg))
