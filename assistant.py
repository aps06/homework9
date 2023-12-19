import re

def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except KeyError:
            result = 'Wrong comand'
        except ValueError:
            result = "Wrong value"
        except IndexError:
            result = "Give me name and phone please"
        return result
    return inner

@input_error
def hello():
    return "How can I help you?"
@input_error
def add(contacts, inputs):
    name, phone = inputs.split()[1], inputs.split()[2]
    if not name in contacts:
        contacts.update({name: phone})
        return contacts
    else:
        raise ValueError
@input_error   
def change(contacts, inputs):
    name, phone = inputs.split()[1], inputs.split()[2]
    if name in contacts:
        contacts.update({name: phone})
        return contacts
    else:
        raise ValueError
@input_error
def phone(contacts, inputs):
    return contacts[inputs.split()[1]]
@input_error
def show_all(contacts):
    contacts_string = ''
    for k, v in contacts.items():
        contacts_string += f'{k}: {v}\n'
    return contacts_string
@input_error
def good_bye():
    return 'Good bye'

COMANDS = {'add': add, 'hello': hello, 'change': change, 'phone': phone, 'show all': show_all,
           'good bye': good_bye, 'close': good_bye, 'exit': good_bye}


def main():    
    contacts = {}
    while True:
        
        inputs = input()
        c = ''
        for i in ['add ', 'hello', 'change ', 'phone ', 'show all',
                  'good bye', 'close', 'exit']:
            if len(c) != 0:
                break
            c = re.findall(fr'^{i}', inputs)
            c = ''.join(c).strip()
        if c in ['add', 'change', 'show all', 'phone'] and len(inputs.split()) <= 3:
            if c == 'phone':
                print(COMANDS[c](contacts, inputs))
            elif c == 'show all':
                print(COMANDS[c](contacts))
            else:
                b = COMANDS[c](contacts, inputs)
                if b.__class__ is dict:
                    contacts = b
                elif b.__class__ is str:
                    print(b)
        elif c in ['hello',  'good bye', 'close', 'exit']:
            a = COMANDS[c]()
            if a == 'Good bye':
                print(a)
                break
        else:
            print('wrong comand')
if __name__ == '__main__':
    main()