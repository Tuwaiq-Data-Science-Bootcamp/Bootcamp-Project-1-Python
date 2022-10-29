# Bootcamp-Project-1-Python

def grocery_store():
    products = {'chips' : "Price : 1$ | Brands : lay\'s , doritos , mrami" ,
                'juice' : "Price : 1$ | Btands : Suntop , Alrabie , Mraie",
                'softdrinks' : "Price : 2$ | Brands : Pepsi , 7Up , Miranda "}


    query = input('Enter your item : ')
    history_chips = 0
    history_juice = 0
    history_softdrinks = 0
    total = 0
    price_juice = 1
    cart_list = []
    while True:
        if query == 'chips':
            print(products['chips'])
            anwser = input('Do like to add any chips to your cart ? press y if Yes and n to go back')
            if anwser == 'y':
                amount = input('How many chips do you like to purchase')
                history_chips +=1
                price_chips = 1 * amount
                total = total + price_chips
                cart_list.append('chips')

            elif query == 'juice':
                print(products['juice'])
                anwser = input('Do like to add any juice to your cart ? press y if Yes and n to go back')
                if anwser == 'y':
                    amount = int(input('How many juice do you like to purchase'))
                    history_juice +=1
                    price_juice *= amount
                    total = total + price_juice
                    cart_list.append('juice')
                
            elif query == 'softdrinks':
                print(products['softdrinks'])
                anwser = input('Do like to add any softdrinks to your cart ? press y if Yes and n to go back')
                if anwser == 'y':
                    history_softdrinks +=1
                    price_softdrinks = 2 * amount
                    total= total + price_softdrinks
                    cart_list.append('softdrink')
            else:
                break


grocery_store()          
                
edit_cart = input('Do you want to show your cart and delete anything press "y" for delete and "n" for pursuing ')

if edit_cart == 'y':
    print(cart_list)
    delete = input('Enter The Item You Want to Delete : ')
    for i in cart_list[:]:
        if delete == 'chips':
            total-=1
            cart_list.remove(delete)
        if delete == 'juice':
            total-=1
            cart_list.remove(delete)
        if delete == 'softdrinks':
            total-=2
            cart_list.remove(delete)


else:
    print('Your order check is {}$ for the whole amount'.format(total))

    print(cart_list)
