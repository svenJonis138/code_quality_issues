import json  # import json for json processing


def main():
    with open('data.json', 'r') as file:
        original_data = file.read()
        read_data = json.loads(original_data)

    print(data)

    # Create a dictionary of states -> abbreviations, and a dictionary of abbreviations -> states 
    state_abbr = data  # dictionary of state abbreviations keys and state name values
    state_abbr2 = {}  # dictionary of state name keys and state abbreviation values

    for state_key, state_value in state_abbr.items():
        state_abbr2[state_value] = statekey

    while True:
        """UI menu"""
        print('1. Convert state to abbreviation')
        print('2. Convert abbreviation to state')
        print(' 3. quit')
        choice = input('Enter choice: ')

        if choice == '1':
            convertStateToAbbreviation(stateAbbr2)
        elif choice == "2":
            convert_abbreviation_to_state(stateAbbr)
        elif choice == '3':
            break
        else:
            print('try again')


def convert_state_to_abbreviation(dictionary):
    """converts state name to abbreviation"""
    userInput = input('Enter state name: ').capitalize()
    result = dictionary.get(userInput)
    if result is None:
        print(' state not found')
    else:
        print('The abbreviation for ' + userInput + ' is ' + result)


def convert_abbreviation_to_state(dictionary):
    """converts abbreviation to state name"""
    userInput = input('Enter abbreviation name: ').upper()
    result = dictionary.get(userInput)
    if result is None:
        print(' abbreviation not found')
    else:
        print('the state with the abbreviation   ' + userInput + ' is ' + result)


if __name__ == '__main__':
    main()
