import re


def input_error(func):
    def inner():
        try:
            func()
        except KeyError:
            print('Enter user name')
            inner()
        except ValueError:
            print("Wrong value")
            inner()
        except IndexError:
            print("Give me name and phone please")
            inner()
    return inner


def add(contacts, inputs):
    name, phone = inputs.split()[1], inputs.split()[2]
    contacts.update({name: phone})
    return contacts


def change(contacts, inputs):
    name, phone = inputs.split()[1], inputs.split()[2]
    contacts[name] = phone
    return contacts


def show_all(dir):
    string = ''
    for k, v in dir.items():
        string += f'{k}: {v}\n'
    return string


def phone(contacts, inputs):
    name = inputs.split()[1]
    return contacts[name]


@input_error
def main():
    contacts = {}
    while True:
        inputs = input().lower()
        comand = ''
        comands = ['add', 'hello', 'change', 'phone', 'show all',
                   'good bye', 'close', 'exit']
        for i in comands:
            if len(comand) != 0:
                break
            comand = re.findall(i, inputs)
            comand = ''.join(comand)
        if comand == 'hello':
            print("How can I help you?")
            continue

        elif comand == 'add':
            contacts = add(contacts, inputs)
            continue

        elif comand == 'change':
            contacts = change(contacts, inputs)
            continue

        elif comand == 'phone':
            print(phone(contacts, inputs))
            continue

        elif comand == 'show all':
            print(show_all(contacts))
            continue

        elif comand in ['good bye', 'close', 'exit']:
            print('Good bye')
            break
        else:
            print('Wrong comand')


if __name__ == '__main__':
    main()
