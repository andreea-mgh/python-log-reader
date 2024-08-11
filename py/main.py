from readfile import *
from functions import *


lines = readFile("example.txt")
logs = extractData(lines)
longlogs = len(logs)


while True:
    option = input()

    if option == "1":
        print(ex1(logs))
    elif option == "2":
        print(ex2(logs))
    elif option == "3":
        print(ex3(logs))
    elif option == "4":
        print(ex4(logs))
    elif option == "5":
        print(ex5(logs))
    elif option == "6":
        print(ex6(logs))
    elif option == "7":
        print(ex7(logs))
    elif option == "8":
        print(ex8(logs))
    elif option == "9":
        print(ex9(logs))
    elif option == "0":
        break
    else:
        print("Invalid option")