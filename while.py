spam = 0
while spam < 5:
 print('Hello, world.')
 spam = spam + 1
# it keeps incrementing for 5 times

 name = ''
#while name != 'your name':
# print('Please type your name.')
# name = input()
# print('Thank you!')
 #execution stops once user types 'your name' as the name.
 
 while True: #infinite loop press ctl+c to stop execution
     #indenting is very crucial, statements inside the while statement should be
     print('Please type your name.')
     name = input()
     if name == 'your name':
         break # break the loop
 print('Thank you!')
