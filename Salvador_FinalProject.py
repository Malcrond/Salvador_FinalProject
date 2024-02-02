import time
from datetime import date


class Console:
    def __init__(self, text):
        self.text = text

    def display(self):
        print(self.text)

    @staticmethod
    def get_input(prompt="INPUT: "):
        return input(prompt)

    @staticmethod
    def sleep(seconds=1):
        time.sleep(seconds)


class ShipStatus:
    @staticmethod
    def display():
        print("---------------[SHIP STATUS]----------------\n"
              "-------------[COOLANT == LOW]---------------\n"
              "-------------[DOCKING == DOCKED]------------\n"
              "-------------[CREW-BAY == ??#$%^4303948583]-\n"
              "-------------[BRIDGE == OBSTRUCTED]---------\n"
              "-[0]-[RETURN]-------------------------------")


class Inbox:
    @staticmethod
    def display():
        print("-----------------[INBOX]--------------------\n"
              "--------------[1]-[MANAGEMENT]--------------\n"
              "--------------[2]-[ENGINE-BAY]--------------\n"
              "--------------[3]-[MURDOCK]-----------------\n"
              "-[0]-[RETURN]-------------------------------")


class Credits:
    @staticmethod
    def display():
        print("------------------[CREDITS]-----------------\n"
              "-[LEAD-DEVELOPER]-[SALVADOR]----------------\n"
              "--------------------------------------------\n"
              "-[0]-[RETURN]-------------------------------\n")


def main():
    sys_console = Console(f"----------[PYRITE SYSTEMS CONSOLE]----------\n"
                          "----------------[1]-[LOGIN]-----------------\n"
                          "----------------[2]-[EXIT]------------------\n"
                          f"---------------[{date.today()}]-----------------")

    sys_console.display()

    while True:
        response = Console.get_input("INPUT: ")
        if response == "1":
            Console.sleep()
            break
        elif response == "2":
            exit()
        else:
            print("---INVALID INPUT---")

    print("-------------[INPUT USERNAME]---------------")
    while True:
        response = Console.get_input("INPUT: ")
        if response.lower() == "admin":
            Console.sleep()
            break
        else:
            print("--------------[INVALID USER]----------------")

    print("-------------[INPUT PASSWORD]---------------")
    while True:
        response = Console.get_input("INPUT: ")
        if response == "12345678":
            Console.sleep()
            Console.sleep()
            print("-------------[ACCESS GRANTED]---------------")
            Console.sleep()
            break
        else:
            print("------------[INVALID PASSWORD]--------------")

    while True:
        admin_console = Console(f"""-----------[PYRITE ADMIN CONSOLE]-----------
----------------[1]-[STATUS]----------------
----------------[2]-[INBOX]-----------------
----------------[3]-[CREDITS]---------------
----------------[0]-[EXIT]------------------
----------------[{date.today()}]----------------""")

        admin_console.display()

        response = Console.get_input("INPUT: ")

        if response == "1":
            Console.sleep()
            while True:
                ShipStatus.display()
                response = Console.get_input("INPUT: ")
                if response == "0":
                    break

        elif response == "2":
            Console.sleep()
            while True:
                Inbox.display()
                response = Console.get_input("INPUT: ")
                if response == "1":
                    while True:
                        print("-HQ HAS REQUESTED THAT ANY WORD OF THE \"VIRAL\" OUTBREAK--\n"
                              "-IN THE MED-BAY BE SILENCED AT ANY COST... -MANAGEMENT-----\n"
                              "-[0]-[RETURN]----------------------------------------------")
                        response = Console.get_input("INPUT: ")
                        if response == "0":
                            break
                elif response == "2":
                    while True:
                        print("-THIS IS ENGINEER M.DOC SPEAKING... WE ARE EXPERIENCING----\n"
                              "-A SEVERE OUTBREAK OF THE POX, ALL OF OUR ENGINE CREW------\n"
                              "-ARE IN A SEVERE STATE OF DECOMMISSION... REQUESTING-------\n"
                              "-ENTRY INTO MEDBAY ASAP -M.DOC-----------------------------\n"
                              "-[0]-[RETURN]----------------------------------------------")
                        response = Console.get_input("INPUT: ")
                        if response == "0":
                            break
                elif response == "3":
                    while True:
                        print("-WE NEED AID, PLEASE... I HAVE A FAMI----------------------\n"
                              "-[0]-[RETURN]----------------------------------------------")
                        response = Console.get_input("INPUT: ")
                        if response == "0":
                            break
                elif response == "0":
                    break

        elif response == "3":
            Console.sleep()
            while True:
                Credits.display()
                response = Console.get_input("INPUT: ")
                if response == "0":
                    break

        elif response == "0":
            while True:
                print("------------[ARE YOU CERTAIN?]--------------\n"
                      "---------------[Y]-----[N]------------------")
                response = Console.get_input("INPUT: ")
                if response.lower() == "y":
                    exit()
                elif response.lower() == "n":
                    break


if __name__ == "__main__":
    main()
