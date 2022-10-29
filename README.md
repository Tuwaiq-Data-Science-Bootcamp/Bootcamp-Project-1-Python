# Bootcamp-Project-1-Python

## Project#1
Based on what you’ve learned until now, create a project of your choosing (impress us
with your imagination). This project must at least satisfy the following minimum requirements:
- Use at least 3 different data types.
- Use lists or dictionaries or tuples or sets.
- Use loops.
- Use functions that return an output.
- Use conditions.
- Use a Lambda function.

## Example#1: An online Grocery Store
Overview : An online store that sells fruits to customers. The customers should be able to
do the following tasks for the store to function properly.

### As a customer I should be able to do the following:
- Browse Products.
- View the product info (summary, specs, price, quantity, etc.)
- Search for Products.
- Get recommendations for my next purchase based on my purchase history.
- Add Products to the shopping cart.
- Remove a product from the shopping cart.
- List the products in my shopping cart.
- Continue to checkout.
- Fill in my address for delivery.
- Get receipt of my purchases.
- Check delivery status.





print('Welcome to the fresh fruits store: \n')

products=['banana','orange', 'papaya','strawberries','apple']

print('***********************************')
print('\t Our products: \n', products)
print('***********************************\n')

quantity={'banana':20,'orange':45,'papaya':10,'strawberries':13,'apple':30}


price={'banana':2.99,'orange':1.5,'papaya':7,'strawberries':56,'apple':1.80}


    
while True:
    choosenProducts=input('Please enter the name of the fruit: \n')    
    
    if choosenProducts not in products:
        print ('Chosse only from the showen menue\n')
        

    for x in products:
            print('\nThe quantity of', choosenProducts, 'in stock is:', quantity[choosenProducts], "Kilogram")
            print('\nThe price for (1 kilo)' ,choosenProducts, 'is:', price[choosenProducts], "SR\n\n")
            
            while True:
                choosenquantity=input('Please enter the quantity you want: \n')
                choosenquantity_Casted_To_Int =int (choosenquantity)
                if choosenquantity_Casted_To_Int>quantity[choosenProducts]:
                    print('No enough quantity\n\n')
                    print('\nThe quantity of' ,choosenProducts, 'in stock is:', quantity[choosenProducts], "Kilogram")
                elif choosenquantity_Casted_To_Int<=0:
                    print('quantity must be greater than zero\n\n')
                    print('\nThe quantity of', choosenProducts, 'in stock is:',quantity[choosenProducts], "Kilogram")
                elif choosenquantity_Casted_To_Int<=quantity[choosenProducts]:
                    Updated_quantity = quantity[choosenProducts] - choosenquantity_Casted_To_Int
                    quantity[choosenProducts] = Updated_quantity                  
                    
                    total_cost = lambda a, b : a * b
                    
                    print('The total cost for',choosenquantity,'KG of',choosenProducts, 'is:', ':' ,total_cost(choosenquantity_Casted_To_Int, price[choosenProducts]), 'SR\n\n\n' )
                    print('Your cart has the following products & quantity:\n','Products: ',choosenProducts,'\nQuantity: ',choosenquantity, '\nTotal cost:' ,total_cost(choosenquantity_Casted_To_Int, price[choosenProducts]), 'SR\n\n' )
               
                    
                    while True:
                        someThingelsecustomerWant=input('Would you like something else?,If so, please  type [CONTINUE] or [QUIT]\n\n')

                        if someThingelsecustomerWant=='CONTINUE':
                            break
                      
                        elif someThingelsecustomerWant=='QUIT':
                            print('Checkout your total is: ', total_cost, '\n\n')
                            break
                    break
                    
          
    
    
 




## Example#2: Strong Personal Password
Overview : A system creates personal random passwords, these passwords should be strong enough and contains capital and small letters, numbers and symbols. Therefore, you need to do the following.
- Save all letters in a list.
- Ask the user about password length.
- shuffle passwords.
- use loops to create a passsword.
- choose a random letter from letters by using random.choice.
- Add a random letter to the password.
- Write a function that add capital letters to the password.
- Write a function that add random numbers to the password.
- Write a function that add symbols to the password.
- Final Randomization to the final pattern.
- Print the Final Password.




import random


print('***********************************')
print('\tPassword generator')
print('***********************************\n\n\n')


#string.ascii_letters
#string.ascii_uppercase, k=2
#string.ascii_lowercase, k=2


lettersList=['a','b','c','d','e','f','g','h','i','j','k','l','n','o','p','q','r','s','t','u','v','w','x','y','z']
digList=[0,1,2,3,4,5,6,7,8,9]
symbList = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '<', '>', '?' ]
password=''

joinAllLists = lettersList + digList + symbList

#random.shuffle(joinAllLists)
#print(joinAllLists)

while True:
    passLength=int(input('\nPlease enter the length of your password:'))

    def myshuffledListfunc():
        random.shuffle(joinAllLists)


        def myRandomfunc():
            print('Your generated Password is:\n ')

            for i in range(0,passLength):
                randFromJoinAllLists=random.choice(joinAllLists)
                password=randFromJoinAllLists
                print(password,end="")
        myRandomfunc()


    myshuffledListfunc()    








