import re

contacts = {}
inputs = None
def input_error(func):
    def inner(contacts):
        try:
            func()
        except KeyError:
            print('Enter comand')
            main(contacts)
        except ValueError:
            print("Wrong value")
            main(contacts)
        except IndexError:
            print("Give me name and phone please")
            main(contacts)
    return inner


def hello():
    print("How can I help you?")

def add():
    global contacts
    if not inputs.split()[1] in contacts:
        contacts.update({inputs.split()[1]: inputs.split()[2]})
    else:
        raise ValueError
    
def change():
    global contacts
    contacts[inputs.split()[1]] = inputs.split()[2]

def phone():
    print(contacts[inputs.split()[1]])

def show_all():
    contacts_string = ''
    for k, v in contacts.items():
        contacts_string += f'{k}: {v}\n'
    print(contacts_string)

def good_bye():
    print('Good bye')
    return True

@input_error
def main(contacts={}):
    COMANDS = {'add': add, 'hello': hello, 'change': change, 'phone': phone, 'show all': show_all,
           'good bye': good_bye, 'close': good_bye, 'exit': good_bye}
    while True:
        global inputs
        inputs = input()
        c = ''
        for i in ['add', 'hello', 'change', 'phone', 'show all',
                  'good bye', 'close', 'exit']:
            if len(c) != 0:
                break
            c = re.findall(fr'^{i}', inputs)
            c = ''.join(c)
        a = COMANDS[c]()
        if a:
            break
if __name__ == '__main__':
    main(contacts)