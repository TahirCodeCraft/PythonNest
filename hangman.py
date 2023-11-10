Name=input("What is your name : ")
print ("Hello, " ,Name, "let's play a word guessing game, hangman!")
print (" ")
print ("The word contain 6 letters")
print ("Start guessing...")
word = "secret"
guesses = ''
turns = 10
while turns > 0:         
    failed = 0                 
    for i in word:      
        if i in guesses:    
            print (i , end='')    
        else:
            print ("_ " ,end='')     
            failed += 1    
    if failed == 0:        
        print ("You won")
        break              
    print('')
    guess =input("guess a character: ") 
    guesses += guess                    
    if guess not in word:  
        turns -= 1        
        print ("Wrong")
        print ("You have", + turns, 'more guesses') 
        if turns == 0:           
            print ("You Lose")
