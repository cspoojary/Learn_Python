#Variable : A reusable container for storing a  value.
#           A variable behaves as of it were the value it contains.

age = 21

print("Age")

print(age)


#string concatenation
print("You are " + str(age) + " years old")
print("You are ", age, "years old")

#f-string
print(f"You are {age} years old")

#Basic Data types
#INTEGER
age = 21
players = 3
quantity =5

print(f"You are {age} years old")
print(f"There are {players} plyaers online")
print(f"You would like to buy {quantity} items")

#FLOAT

gpa = 3.2
distance = 2.5
price = 10.99

print(f"Your gpa is {gpa}")
print(f"Your ran {distance}Km")
print(f"The price is ${price}") 

#STRING
name = "Bro"
food = "pizza"
email = 'Bro123@gmail.com '

print(f"Hello {name}")
print(f"You like {food}")
print(f"Yor email is:{email}") 

#BOOLEAN
online = True
for_sale = False
running = True

print(f"Are you online?: {online}")
print(f"Is the item for sale?: {for_sale}")
print(f"Game running: {running}")

if running:
    print("The game is running")
else:
    print("The game is ove")
