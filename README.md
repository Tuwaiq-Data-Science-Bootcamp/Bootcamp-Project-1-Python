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

# Use at least 3 different data types.
#1-Text Type
q1="1- What is the largest big cat?"
q2="2- What land animal can open its mouth the widest?"
q3="3- What is the largest animal on Earth?"
q4="4- What is the only flying mammal?"
q5="5- What is an animal called that eats plants and meat?"
q6="6- Why do sea otters hold hands?"

#2-Numeric Type
global score
score=0
qNum=1
global questions
questions=6

#Use lists or dictionaries or tuples or sets.
list1=["Lion","Tiger","Cheetah"]
list2=["Alligator","Baboon","Hippo"]
list3=["The African elephant","The blue whale","The giant squid"]
list4=["The bat","The flying squirrel","The bald eagle"]
list5=["Carnivore","Herbivore","Omnivore"]
list6=["To show they are in the same family","So they do not float away when they are sleeping","Because they are playing"]

ansLst={2:2,3:3,4:2,5:1,6:3,7:2}


#Use functions that return an output.
def checkAns(ans,qNum):
                        #3-Boolean Type
                        win=False
                        #Use conditions.
                        if ans==ansLst[qNum]: 
                                          win=True
                                          global score
                                          score=score+1
                    
                        return win
#Use functions that return an output.
def printQs(lst1,lst2):
                       print(lst1,"\n")
                       row=1
                       for i in lst2:
                                      print(row,"- ",i)
                                      row=row+1
                       
        
#Use functions that return an output.
def printQ(qNum):
                if qNum==1:
                           printQs(q1,list1)
                if qNum==2:
                            printQs(q2,list2)
                if qNum==3:
                            printQs(q3,list3)
                if qNum==4:
                            printQs(q4,list4)
                if qNum==5:
                            printQs(q5,list5)
                if qNum==6:
                            printQs(q6,list6)
#Use functions that return an output.
def getScoreMsg(score):
                        global questions
                       
                        remain=questions-score
                        msg=""
                        if remain==0: 
                                     msg="Well Done! You got a perfect score"
                        elif remain == questions:
                                                msg="Try again!"
                                              
                        else:
                             msg="You got "+str(score)+" questions right out of "+str(questions)+" questions."
                             
                             
                      
                        return msg


name=input("Enter your name:")  
print("Welcome", name)
#Use loops.               
while qNum<questions:
            printQ(qNum)
            qNum=qNum+1
            ans=input("Enter number of your choice:")
            while str(ans).isdigit()==False or int(ans)<=0 or int(ans)>3 :
                                                                          ans=input("This is invalid number\nEnter a valid choice:")
                        
            if int(ans)>0:  
                          if checkAns(int(ans),qNum):
                                                     print("Correct Answer")
                          else:
                               print("Wrong Answer!")
                          
print("Your score is:",score)
print(getScoreMsg(score))

#Use a Lambda function.
precent = lambda x : (x/questions)*100
print("Your percentage is ",precent(score),"%")
