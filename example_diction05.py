dic = {
    'Trousers':{
        '36':['blue', 'red', 'yellow'],
        '38':'green',
        '40':['yellow', 'blue']
    },
    'Scarf':{
        'rectangle': ['blue', 'red', 'yellow'],
        'triangle' : ['pink', 'purple', 'yellow'],
        'square' : ['green', 'light blue']
    },
    'skirt':{
        'long': ['black'],
        'short':['black', 'gray'],
        'medium': ['blue', 'red', 'yellow'],
    }
}

color = input('What color do you want: ')

def get_input(ap_list):
    print('product',ap_list)
    ap = input('Please enter a product: ')
    while not ap_list.__contains__(ap):
        ap = input('Please enter a product: ')
    else:
        print('catagory', dic[ap].keys())
        ac = input('Please enter a catagory: ')
        #print(dic[ap].keys())
        if color in dic[ap][ac]:
            print('yes')
        else:
            print('no')




get_input(dic.keys())


#catagory = input('Please enter a catagory: ')












#print((dic[product][catagory]))