
def menu(functionChoices: list, menuTitle: str, menuPrompt: str) -> None:
    """Prints a menu of choices and prompts the user to make a selection."""
    print(menuTitle)
    for i in range(len(functionChoices)):
        print(str(i+1)+". "+functionChoices[i][0])
    print("0. Exit")
    while True:
        try:
            choice = int(input(menuPrompt))
            if choice < 0 or choice > len(functionChoices):
                raise ValueError
            # print(choice)
            if choice == 0:
                return
            params = []
            for i in range(len(functionChoices[choice-1][2])):
                params.append(input(functionChoices[choice-1][2][i]))
            functionChoices[choice-1][1]( *params)
        except ValueError:
            print("Invalid choice. Try again.")
        except Exception as e:
            print(e)
            print("Something went wrong. Try again.")
        
        