dic = {
    'Trousers':{
        '36':['blue', 'red', 'yellow'],
        '38':'green',
        '40':['yellow', 'blue']
    },
    'Scarf':['orange', 'red', 'green'],
    'skirt':{
        'long': 'black',
        'short':['black', 'gray'],
        'medium': ['blue', 'red', 'yellow'],
    }
}
product = input('Please enter a product: ')
def color_dic(product):
    if product == (dic['Trousers']):
        Size = input('Please choose a size between 36, 38, 40')
        if Size == '36':
            Color = input('Please enter the color you desire to buy')
            if Color == 'blue' or 'red' or 'yellow':
                print('The color your desire to buy is available')
            else:
                print('The color you desire to buy is unavailable')
color_dic(product)













