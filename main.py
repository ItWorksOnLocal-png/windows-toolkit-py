from banner import banner
import os
import time
from click import pause


class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[31m'
    END = '\033[0m'


def shutdown():
    if os.name == 'nt':
        try:
            timeout = input("\nHow many seconds till shutdown? ")
            timeout = int(timeout)

            os.system(f'shutdown /s /t {timeout} /c "Your computer will shutdown in {timeout} seconds"')

            validation = True
            while validation:
                abort_shutdown = input("\nDo you want to abort the shutdown? (y/n): ")

                if abort_shutdown in ['y', 'yes', 'yeah', 'Y', 'YES', 'YEAH']:
                    os.system('shutdown /a')
                    print("\nPlease wait...")
                    time.sleep(1)
                    print(f"\n{bcolors.GREEN}**Shutdown aborted successfully!**{bcolors.END}")
                    validation = False

                elif abort_shutdown in ['n', 'no', 'nah', 'nono', 'N', 'NO', 'NAH', 'NONO']:
                    print("\nOkay! You just have to wait for the shutdown! The program will exit now!")
                    time.sleep(.5)
                    quit()

                else:
                    print(f"\n{bcolors.WARNING}Not a valid response!{bcolors.END}")
                    time.sleep(.5)
                    validation = True

        except ValueError:
            print("\n***Your input has to be in seconds(numbers)***")
            shutdown()
    else:
        print(f"{bcolors.WARNING}This feature is only available for Windows{bcolors.END}")
# print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")


def restart():
    if os.name == 'nt':
        try:
            timeout = input("\nHow many seconds till restart? ")
            timeout = int(timeout)

            os.system(f'shutdown /r /t {timeout} /c "Your computer will restart in {timeout} seconds"')

            validation = True
            while validation:
                abort_restart = input("\nDo you want to abort the restart? (y/n) ")

                if abort_restart in ['y', 'yes', 'yeah', 'Y', 'YES', 'YEAH']:
                    os.system('shutdown /a')
                    print("\nPlease wait...")
                    time.sleep(1)
                    print("\n**Restart aborted successfully!**")
                    validation = False

                elif abort_restart in ['n', 'no', 'nah', 'nono', 'N', 'NO', 'NAH', 'NONO']:
                    print("\nOkay! You just have to wait for your computer to restart! The program will exit now!")
                    time.sleep(.5)
                    quit()

                else:
                    print(f"\n{bcolors.WARNING}Not a valid response!{bcolors.END}")
                    time.sleep(.5)
                    validation = True

        except ValueError:
            print("\n***Your input has to be in seconds(numbers)***")
            restart()
    else:
        print("This feature is only available for Windows")


def logoff():
    if os.name == 'nt':
        print("\n***PLEASE SAVE YOUR WORK BEFORE LOGGING OFF BECAUSE ANY UNSAVED WORK WILL BE LOST!!!***")
        time.sleep(5)
        validation = True
        while validation:
            confirmation = input('''\n***PLEASE NOTE THAT YOU WILL BE LOGGED OUT IMMEDIATELY AND CAN'T BE CANCELLED, 
            DO YOU STILL WANT TO EXECUTE IT?(yes/no): ''')

            if confirmation in ['y', 'yes', 'yeah', 'Y', 'YES', 'YEAH']:
                print("Logging  off...")
                time.sleep(1)
                os.system('shutdown /l')
                validation = False

            elif confirmation in ['n', 'no', 'nah', 'nono', 'N', 'NO', 'NAH', 'NONO']:
                print("\nOkay, going back to the main menu, please wait...")
                time.sleep(1)
                main()

            else:
                print(f"\n{bcolors.WARNING}Not a valid response!{bcolors.END}")
                time.sleep(.5)
                validation = True
    else:
        print("This feature is only available for Windows")


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')


def whoami():   # The only feature that works on Linux
    clear_screen()
    print("\n**This feature will tell you what user is currently logged in**\n")

    print("========================================")
    print("The currently logged user is:")
    os.system('whoami')
    print("========================================")
    pause(f"\n{bcolors.BLUE}Press any key to go back to the main menu...{bcolors.END}")

    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    main()


def control_panel():
    if os.name == 'nt':
        print("Launching Control Panel...")
        time.sleep(1)
        os.system('control')
        pause(f"\n{bcolors.BLUE}Press any key to go back to the main menu...{bcolors.END}")

        if os.name == 'nt':
            os.system('cls')
        elif os.name == 'posix':
            os.system('clear')
        main()

    else:
        print("This feature is only available for Windows")


def os_version():
    if os.name == 'nt':
        clear_screen()
        print("System information retrieved:")
        print("===============================================================")
        os.system('systeminfo | findstr /B /C:"OS Name" /C:"OS Version"')
        print("===============================================================")
        pause(f"\n{bcolors.BLUE}Press any key to go back to the main menu...{bcolors.END}")

        if os.name == 'nt':
            os.system('cls')
        elif os.name == 'posix':
            os.system('clear')
        main()

    else:
        print("This feature is only available for Windows")


def main():

    banner()

    print('''\n
    (1) Shutdown Computer (Only for Windows)
    (2) Restart Computer (Only for Windows)
    (3) User Logoff (Only for Windows)
    (4) Who Am I? (Windows & Linux)
    (5) OS Version (Only for Windows)
    (6) Open Control Panel (Only for Windows)
    (0) Quit Program
    \n''')

    try:
        user_choice = input("Choose an option: ")
        user_choice = int(user_choice)

        if user_choice == 0:
            print("Goodbye!")
            time.sleep(.5)
            quit()

        if user_choice == 1:
            shutdown()
        elif user_choice == 2:
            restart()
        elif user_choice == 3:
            logoff()
        elif user_choice == 4:
            whoami()
        elif user_choice == 5:
            os_version()
        elif user_choice == 6:
            control_panel()
        else:
            print("***Invalid choice, try again!***")
            main()

    except ValueError:
        print("***Your choice has to be one a number!***")
        main()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        if os.name == 'nt':
            os.system('cls')
        elif os.name == 'posix':
            os.system('clear')
        print('\n\nProgram interrupted by user, quitting...')
        time.sleep(1)
        quit()
