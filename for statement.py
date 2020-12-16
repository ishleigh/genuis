i=2
print('My name is:')
for i in range(3):
    print('Ashy ('+str(i)+')')

#the above program using a while loop
print('My age is:')
i = 0
while i < 5:
 print('I am  (' + str(i) + ')')
 i = i + 1


#total = 0
#for num in range(20): # executes 19 times
 #   total = total + num
#print(total) #calcuate the sum off the numbers from 0 to 19

#Guass finding when asked to add the numbers from 1-100
#there are 50 sets and a reminder 50 each adding to 100
#This leaves out a 50 in the middle. (50x100)+50

total = 0
for num in range(101): #executes 100 times
     total = total + num
print(total) 


# the range func can have multiple aurguments
for i in range(12, 16):
 print(i) #prints numbers 12,13,14 and 15

for i in range(0, 10, 2):
 print(i) # 0 is the start and 10 is the stop, 2 is the step argument
 #the output increases by 2

for i in range(5, -1, -1):
 print(i)# displays 5,4, 3, 2, 1, 0
