import sys

menu ={'1':'Wings','2':'Cookies','3':'Spring Rolls',
       '4':'Salmon','5':'Steak','6':'Meat Tornado',
       '7':'Ice Cream','8':'Cake','9':'Pie',
       '10':'Coffee','11':'Tea','12':'Unicorn Tears'}
def welcom_msg():
    print('**************************************')
    print('**    Welcome to the Snakes Cafe!   **')
    print('**    Welcome to the Snakes Cafe!   **')
    print('**')
    print('** To quit at any time, type "quit" **')
    print('**************************************',"\n")

    print('Appetizers')
    print('----------',"\n")
    print(menu["1"])
    print(menu["2"])
    print(menu["3"],"\n")

    print('Entrees')
    print('--------',"\n")
    print(menu["4"])
    print(menu["5"])
    print(menu["6"],"\n")

    print('Desserts')
    print('--------',"\n")
    print(menu["7"])
    print(menu["8"])
    print(menu["9"],"\n")

    print('Drinks')
    print('-------',"\n")
    print(menu["10"])
    print(menu["11"])
    print(menu["12"],"\n")

    print('**************************************',"\n")
    print('** What would you like to order? **',"\n")
    print('**************************************',"\n")
welcom_msg()

requested = input(">")

def check_to_exit(msg):
    if msg == 'quit':
        sys.exit()
check_to_exit(requested)

def orderd_list(order):
    orders = []
    while order != 'quit':
        if order in menu.values():
            orders.append(order)
            print(f'** {orders.count(order)} order of {order} have been added to your meal **')
        order = input(">")
    
orderd_list(requested)