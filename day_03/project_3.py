print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")

left_right = input("left or right ").lower()

if left_right == 'left':
    swim_wait = input("swim or wait ").lower()
    if swim_wait == 'wait':
        door = input("Which door? Red, Blue or Yellow ").lower()
        if door == 'Red':
            print("Game Over")
        elif door == 'Blue':
            print("Game Over")
        else:
            print("You Win!")
    else:
        print("Game Over")
else:
    print("Game over")

