import pygame  # Import the Pygame library, which is used for game development.

# Initialize the Pygame library.
def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))  # Create a window of size 400x400 pixels.

# Function to check if a specific keyboard key is pressed.
def getKey(keyName):
    ans = False  # Initialize the 'ans' variable to False (indicating the key is not pressed).

    for eve in pygame.event.get():
        pass  # Iterate through Pygame events and do nothing (events are not used in this function).

    keyInput = pygame.key.get_pressed()  # Get a list of boolean values representing the state of all keys.
    myKey = getattr(pygame, 'K_{}'.format(keyName))  # Dynamically get the key code for the specified key name.

    if keyInput[myKey]:
        ans = True  # If the specified key is pressed (based on the key code), set 'ans' to True.

    pygame.display.update()  # Update the display (not necessary in this context).

    return ans  # Return 'ans,' which is True if the key is pressed, or False if it's not.

#def main():

    # #Check1
    # print(getKey("a")) #checks if A is pressed in the keyboard

    # #Check2
    # if getKey("LEFT"):
    #     print("Left key pressed")
    #
    # if getKey("RIGHT"):
    #     print("Right key pressed")

    # # Check3 - Code to test the functionality of KeyPressModule.py
    # while True:
    #     key_pressed = getKey("s")
    #     print(key_pressed)


# if __name__ == '__main__':
#
#     init()
#
#     while True:
#         main()