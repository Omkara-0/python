name = input('Enter your name: ')
i=int(input('Number of subject that you have studied:'))
p=1
m=0
while p<=i:
    a=int(input('Enter your marks in subject '+ str(p) +' out of 100 '))
    p=p+1
    m=int(a)+m
    
print('Total marks:' + str(m))  
p = (print('percetage :' + str(m/i)))
Q = int(m/i)


if Q >=95:
    print('your grade is A+')
elif  Q<95 and Q>=90:
    print('your grade is A')
elif  Q<90 and Q>=80:
    print('your grade is B')
elif  Q<80 and Q>=60:
    print('your grade is C')
elif  Q<60 and Q>=50:
    print('your grade is D')
elif  Q<50 and Q>=40:
    print('your grade is E')
else :
    print('you are fail')