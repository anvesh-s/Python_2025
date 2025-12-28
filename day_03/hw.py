print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("you can go ahead and ride it")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("child tics are $5.")
    elif age <= 18:
        bill = 7
        print("youth pay $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok, have a free ride on us!")
    else:
        bill = 12
        print("adults pay $12.")

    wants_photo = input("Do you want to have a photo taken? y for yes and n for n")
    if wants_photo == 'y':
        bill = bill + 3
    
    print(f"your final bill is {bill}")
else:
    print("grow taller biatch!")

    


# modulo 

print(10%5)
print(10%3)

#odd or even 

num = int(input("enter your number: "))

if num % 2 == 0:
    print("even")
else:
    print("odd")


# logical operatos
# A and B = 
