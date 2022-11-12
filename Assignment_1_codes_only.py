'''Q16. Write a code that gives following as an output.
```
iNeuroniNeuroniNeuroniNeuron'''

print("iNeuron"+"iNeuron"+"iNeuron"+"iNeuron")

'''Q17 Write a code to take a number as an input from the user and check if the number is odd or even.'''

num = input("Please enter a number")

if int(num)%2==0:
    print("The number entered is even")
else:
    print("The number entered is even odd")

'''Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".'''

Age = input("Please eneter your age: ")
if int(Age)>=18:
    print("I can vote")
else:
    print("I can't vote")

'''Q23. Write a code that displays the sum of all the even numbers from the given list.
```
numbers = [12, 75, 150, 180, 145, 525, 50]'''

numbers = [12, 75, 150, 180, 145, 525, 50]

even_sum=0

for i in numbers:
    if i%2==0:
        even_sum+=i
print("The sum of even numbers in the list is: ",even_sum)

'''Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.
'''
my_list = []
for i in range(1,4):
    my_list.append(int(input("Please eneter the number")))

print('The maximum number out of 3 inputs is: ', max(my_list))

'''Q25. Write a program to display only those numbers from a list that satisfy the following conditions

- The number must be divisible by five

- If the number is greater than 150, then skip it and move to the next number

- If the number is greater than 500, then stop the loop
```
numbers = [12, 75, 150, 180, 145, 525, 50]'''

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i>500:
        break
    if i%5==0:
        if i>150:
            continue
        print("the number is: ", i )

