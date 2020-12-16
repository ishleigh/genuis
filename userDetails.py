print('Hello world!')
print('What is your name?') # ask for their name
myName = input() #assigns the in put from the user to the variable myName
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName)) #get the number of characters in the string
print('What is your age?') # ask for their age
myAge = input() #waits for input from the user
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
#str() converts the interger into string so they can be joined together
