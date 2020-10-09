##Questions Dictionary
questions = {
            'Which method can be used to return a string in upper case letters?':            
    ('\na. upperCase()\nb. uppercase()\nc. upper()\nd. toUpperCase()\n', 'c'),
            'What is the correct file extension for Python files?':         
    ('\na. .py\nb. .pt\nc. .pyt\nd. .pyth\n', 'a'),
    'What is the correct syntax to output the type of a variable or object in Python?':           
    ('\na. print(type(x))\nb. print(typeof(x))\nc. print(typeOf(x))\nd. print(typeof x)\n', 'a'),
    'Which method can be used to remove any whitespace from both the beginning and the end of a string?':
            ('\na. strip()\nb. trim()\nc. len()\nd. ptrim()\n', 'a'),
    'Which method can be used to replace parts of a string?': 
    ('\na. replace()\nb. switch()\nc. replaceString()\nd. repl()\n', 'a'),
    'Which of these collections defines a LIST?':  
    ('\na. {"apple","banana","Cherry"}\nb. ["apple","banana","Cherry"]\nc. ("apple","banana","Cherry")\nd. {"name":"apple","color":"red"}\n', 'b'),
    'Which of these collections defines a TUPLE?':
        ('\na. {"apple","banana","Cherry"}\nb. ["apple","banana","Cherry"]\nc. ("apple","banana","Cherry")\nd. {"name":"apple","color":"red"}\n', 'c'),
    'Which of these collections defines a SET?':
        ('\na. {"apple","banana","Cherry"}\nb. ["apple","banana","Cherry"]\nc. ("apple","banana","Cherry")\nd. {"name":"apple","color":"red"}\n', 'a'),
    'Which collection is ordered, changeable, and allows duplicate members?':
        ('\na. LIST\nb. TUPLE\nc. SET\nd. DICTIONARY\n', 'a'),
    'How do you start writing a while loop in Python?':
        ('\na. while x > y:  \nb. while (x > y)\nc. while x > y {\nd. x > y while {\n', 'a'),
    'Which statement is used to stop a loop?':  
    ('\na. stop\nb. break\nc. exit\nd. return\n', 'b'),
    'Which operator can be used to compare two values?':
        ('\na. =\nb. ==\nc. <>\nd. ><\n', 'b')
            }

## For asking questions through questions dictionary

import random

def asking_questions(questions):
    item=random.choice(list(questions.items()))
    question=item[0]
    (options,answer)=item[1]
    print(question,options)
    choice=input("\n Hit \'a\', \'b\' , \'c\' , \'d\' for ur answer\n")
    return (choice,answer)

##For to Check User Choice is correct or not

def checking_solution():
    points=0
    tries=0
    for qno in range(3):
        while True:
            choice,answer=asking_questions(questions)
            if(choice not in {'a','b','c','d'}):
                print("INVALID INPUT PLEASE ENTER ONLY IN a or b or c or d for ur question!")
            elif(choice==answer):
                print("WOW! Congratulations Your choice is Correct!!")
                points=points+1
                stop_asking=False
                break
            elif(tries==1):
                print("Ohh Sorry!! You ran out of your attempts")
                stop_asking=True
                break
            else:
                tries+=1
                print("Your Choice is Wrong!!! Please Try Again.")
        if(stop_asking):
            break
    return points
            
##For total 3 rounds each round has 3 random questions through that we can calculate final score

roundNo=1
totalScore=0
while(roundNo<=3):
    print(f"Welcome to Round {roundNo}")
    print("In this sec u have 3 questions to answer if any one is correct ur r eligible to next round!")
    print("\n")
    ##Asking questions from questions dict
    #Calling  asking_questions() through checking_solution() for to ask questions
    result=checking_solution()
    totalScore+=result

    if(result!=0):
        print("\n")
        print(f"You have earned for {roundNo} round points are {result}")
    
    ##If result is > 1 then you are eligible to next round for that 
    #Below if stmt to check
    
    if(result>1):
        roundNo+=1
        if(roundNo<=3):
            print(f"Woww!! You are eligible to {roundNo} round Congratulations for reaching to next Level")
            print("\n")

            continue
    else:
        print("Ohh!! Sorry You have not reached our limit Dont Worry Please Try Again Later")
        break
print("\n")

print(f"Total Score You have earned for 3 rounds as  {totalScore}")
    




