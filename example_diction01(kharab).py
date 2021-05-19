x = input("Please enter the command: ")
def command(x):
    if x == 'update':
        x = input("Please enter a name and a phone number: ")
        dic.update(x)
    if x == 'delete':
        x = input("Please enter a name: ")
        dic.pop(x)


dic = {
    'Amirreza': {
        'Hamrahe aval' :'091452684',
        'Irancell': '09365557',
    'Alireza': '0914425975' 
    },
}

command(x)