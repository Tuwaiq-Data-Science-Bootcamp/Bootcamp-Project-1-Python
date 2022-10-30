def friends_game():
    
    character = ('Monica' , 'Ross' , 'Rachel' , 'Chandler' , 'Phoebe' , 'Joey')
    
    
    print("Welcome to F.R.I.E.N.D.S game!!")
    print("The game is : A caption will pop up and you have guess the character that said this particular caption ")
    
    monica_cap = ["I KNOW !!!" , "THAT'S NOT EVEN A WORD !!! " , "Chandler .. WHAT IS THE MATTER WITH YOUR FACE??!", "OK, just to be clear, comedy with the plates will not be well-recieved." ,"Ross married Rachel in vegas and got divorced AGAIN!!"]
    rachel_cap = ["AAHHH Salamon Skin Roll.." , "You fell ASLEEP !!!" , "I got off the plane ..." , "OH.. look who it is, My husband the apple of my eye", "He's a transponster"]
    joey_cap = ["How you doin' " , "Could I be wearing anymore clothes? " , "It's a moo point !" , "I'm curvy and I like it !!" , "London Baaaabe !!!", "Why god why !! we had a deal let the others grow old not me"]
    chandler_cap = ["What did I marry into !" , "Was that place THE SUN ??" , "OH MY GOD YoU ALmoSt GavE mE A hEarT AtTaCk" , "I'm sorry we don't have your sheep", "Wooh-Paah!!"]
    phoebe_cap = ["Smelly cat Smelly cat .. What are they feeding you" , "Not even have a pla-" , "MY EYES MMYY EYEEYYSS !!!" , "E as an ello there mate", "Have I gone deaf???"]
    ross_cap = ["I'm fine TOTALLY FINE", "It taste like feet" , "PIVOT PIVOT PIVOT PIVOT" , "Unagi.." , "You had rambled on for 18 pages FRONT AND BACK !!!"]
    
    questions = ["It taste like feet","I KNOW !!!","What did I marry into !","Smelly cat Smelly cat .. What are they feeding you",
                "THAT'S NOT EVEN A WORD !!! ", "AAHHH Salamon Skin Roll..","Was that place THE SUN ??", "It's a moo point !",
                "Unagi..", "You fell ASLEEP !!!", "Not even have a pla-", "Chandler .. WHAT IS THE MATTER WITH YOUR FACE??!" ,
                "Could I be wearing anymore clothes? ", "I got off the plane ...","I'm fine TOTALLY FINE", "MY EYES MMYY EYEEYYSS !!!",
                "OK, just to be clear, comedy with the plates will not be well-recieved.","PIVOT PIVOT PIVOT PIVOT","I'm curvy and I like it !!",
                "OH MY GOD YoU ALmoSt GavE mE A hEarT AtTaCk","E as an ello there mate", "London Baaaabe !!!",
                "OH.. look who it is, My husband the apple of my eye","Have I gone deaf???","You had rambled on for 18 pages FRONT AND BACK !!!",
                "He's a transponster","Why god why !! we had a deal let the others grow old not me","Ross married Rachel in vegas and got divorced AGAIN!!",
                "Wooh-Paah!!","I'm sorry we don't have your sheep"]
    
    points = 0
    for q in questions[:]:
        print("Who said : " + q)
        print(character)
        answer = input('Enter Which Friend Said That : ')
        
        if q in monica_cap and answer.capitalize() == 'Monica':
            print("it's correct it was Monica!!")
            points+=1
            
        elif q in ross_cap and answer.capitalize() == 'Ross':
            print("it's correct it was Ross!!")
            points+=1
            
        elif q in chandler_cap and answer.capitalize() == 'Chandler':
            print("it's correct it was Chandler!!")
            points+=1
            
        elif q in phoebe_cap and answer.capitalize() == 'Phoebe':
            print("it's correct it was Phoebe!!")
            points+=1
            
        elif q in joey_cap and answer.capitalize() == 'Joey':
            print("it's correct it was Joey!!")
            points+=1
        
        elif q in rachel_cap and answer.capitalize() == 'Rachel':
            print("it's correct it was Rachel!!")
            points+=1
        else:
            print("Sorry you're wrong ..")
        
    print("I hope you had fun you're points are {} , GOOD JOB!!".format(points))
    
    
friends_game()
