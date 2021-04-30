""" a program to convert a state abbreviation to state name or vice-versa """
import json  # import json for json processing


def main():
    """ Create a dictionary of states -> abbreviations,
    and a dictionary of abbreviations -> states """
    with open('data.json', 'r') as file:
        original_data = file.read()
        read_data = json.loads(original_data)

    abbreviations_to_state_name = read_data  # dictionary of state abbreviations keys and state name values
    state_name_to_abbreviations = {}  # dictionary of state name keys and state abbreviation values

    for state_key, state_value in abbreviations_to_state_name.items():
        state_name_to_abbreviations[state_value] = state_key

    while True:
        print('1. Convert state to abbreviation')
        print('2. Convert abbreviation to state')
        print('3. quit')
        choice = input('Enter choice: ')

        if choice == '1':
            convert_state_to_abbreviation(state_name_to_abbreviations)
        elif choice == '2':
            convert_abbreviation_to_state(abbreviations_to_state_name)
        elif choice == '3':
            break
        else:
            print('try again')


def convert_state_to_abbreviation(dictionary):
    """ converts state name to abbreviation """
    user_input = input('Enter state name: ').capitalize()
    result = dictionary.get(user_input)
    if result is None:
        print(' state not found')
    else:
        print(f'The abbreviation for {user_input} is {result}')


def convert_abbreviation_to_state(dictionary):
    """ converts abbreviation to state name """
    user_input = input('Enter abbreviation name: ').upper()
    result = dictionary.get(user_input)
    if result is None:
        print(' abbreviation not found')
    else:
        print(f'the state with the abbreviation {user_input} is {result}')


if __name__ == '__main__':
    main()
