while True:
     print('Who are you?')
     name = input()
     if name != 'Joe':
        continue #will iterate until the condition is met
     print('Hello, Joe. What is the password? (It is a fish.)')
     password = input()
     if password == 'swordfish':
         break #stops and goes back to the beginning of the loop
print('Access granted.')#executed when the conditions are met
 
