contact = {
    'Amirreza' : '09101040436',
    'Amir' : '0914599455'
}
action = input("Please enter an action: ")

def edit_contact(action):
    if action == 'del':
        person_name = input('Please enter a name: ')
        contact.pop(person_name)
    elif action == 'read':
        person_name = input('Please enter a name: ')
        print(contact[person_name])
    elif action == 'add' or 'update':
        person_name = input('Please enter a name: ')
        person_number = input('Please enter a number: ')
        contact.update({person_name : person_number})
   
edit_contact(action)
print(contact)
