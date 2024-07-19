'''cbrew.py helps the user to make cold brew coffee'''
import sys
import signal
import time
from textwrap import dedent


def make_choice():
    '''Let the user decide what type of CB he plans to prepare'''
    intro = dedent('''\
                    What type of Cold Brew to you want to brew?

                    ➀ Brewing a concentrate         (ratio, 1:5)
                    ➁ Brewing a "Ready to drink CB" (ratio, 1:14)
                    ➂ Diluting concentrate to CB    (ratio, 1:3)
                    ➃ Quit''')

    print(f'{intro}\n')
    choice = input("Make your choice: ")

    print()
    return choice


def user_choice(choice):
    '''Prepare recipe according to user's preference'''
    match int(choice):
        # Concentrate CB.
        case 1:
            ratio = 5
            print(f"\nTo prepare a concentrate, you'll need {brewing(ratio)} liter of water.")
        # Ready to drink CB.
        case 2:
            ratio = 14
            print(f"\nTo prepare ready to drink CB, you'll need {brewing(ratio)} liter of water.")
        # Concentrate diluting.
        case 3:
            ratio = 3
            print(f"\nTo dilute it, you'll need {diluting_concentrate(ratio):.1f} liter of water.")
        case 4:
            print("Bye.")
            cleanup(2)
        case _:
            print("Invalid choice, bye.")
            cleanup(3)


def brewing(ratio):
    '''Calculate amount of water related to coffee beans'''
    beans = input("How much coffee beans to use (g): ")
    water = (int(beans) * ratio) / 1000
    return water


def diluting_concentrate(ratio):
    '''Calculate amount of water to add to concentrate'''
    concentrate = input("How much concentrate do you have (ml): ")
    water = (int(concentrate) * ratio) / 1000
    return water


def cleanup(exit_code):
    '''Ensure clean exit'''
    # Ctrl-c.
    if interrupt_received:
        print("\nUser exit: cleaning process...")
        time.sleep(1)
        sys.exit(exit_code)

    # Choice exit.
    if exit_code in (2, 3):
        time.sleep(1)
        sys.exit(exit_code)

    # Normal exit.
    else:
        print("\n🥶 Enjoy your Cold Brew 🥶\n")
        time.sleep(1)
        sys.exit(exit_code)


def sigint_handler(signum, frame):
    '''Handle ctrl-c'''
    global interrupt_received
    interrupt_received = True

    if interrupt_received:
        cleanup(1)


def main():
    '''Main process to CB'''
    choice = make_choice()
    user_choice(choice)
    cleanup(0)


signal.signal(signal.SIGINT, sigint_handler)
interrupt_received = False

if __name__ == "__main__":
    main()
