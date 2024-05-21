import random

def shape_game():
    print("Welcome to the Shape Guessing Game!")

    # Define a list of shapes
    shapes = ["circle", "square", "triangle", "rectangle"]

    # Randomly choose a shape
    secret_shape = random.choice(shapes)

    attempts = 0
  
    while True:
        # Get player's guess
        guess = input("Enter your guess (circle, square, triangle, rectangle): ").lower()
        attempts += 1

        # Check if the guess is correct 
        if guess == secret_shape:
            print(f"Congratulations! You guessed the correct shape '{secret_shape}' in {attempts} attempts.")
            break
        else:
            print("Incorrect guess! Try again.")

if __name__ == "__main__":
    shape_game()
