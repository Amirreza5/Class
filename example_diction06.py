menu = {
    'pizza' :{
        'price' : '4.99$',
        'TimeToMake' : '30m',
        'ingredient' : ['cheese', 'sausage', 'sause', 'Pizza Dough'] 
    },
    'hamburger' : {
        'price' : '3.99$',
        'TimeToMake' : '20m',
        'ingredient' : ['beef', 'bread', 'sause', 'tomato']   
    },
    'french fries' : {
        'price' : '1.99$',
        'TimeToMake' : '10m',
        'ingredient' : ['potato', 'sause']
    }
}
product = input('Which product do you desire: ')

def product_input(product):
    if product == 'pizza' :
        print(menu['pizza'])
    elif product == 'hamburger':
        print(menu['hamburger'])
    elif product == 'french fries':
        print(menu['french fries'])
product_input(product)