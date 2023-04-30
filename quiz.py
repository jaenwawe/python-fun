
import random

def question():

    questions = {
        "year": ["2023" ,"What is the current year YYMM?\n"],
        "video": ["game","Finish this sentence.  Mario Brothers is a video\n"],
        "lol": ["laugh out loud","What does lol stand for?\n"],
        "gm": ["Good Morning","If someone texts you gm at 10am, what does it stand for?\n"],
        "agua": ["water", "What does 'agua' mean in english?\n"]
        }
    
    key_list = ["year", "video", "lol", "gm","agua"]

    number = random.randint(0,4)
    question_key= key_list[number]
    

    return [questions[question_key],question_key]


def main():
    print("Thank you for coming to the quiz!")
    interest = {
      "y": True,
      "yes": True
    }




    interested = input("Are you interested in this quiz?\n")

    if  interested.lower() in interest:
        name = input("What is your name?\n")
        print("Great! Let's do this " +name+"!")
        quiz = question()
        print(quiz)
        answer= quiz[0][0].lower() 
        response = input(quiz[0][1]).lower();
        print(answer)

        
        score=0
        
        if answer == response:
            print("Great! " +response+ " was correct!")
            score=+1
            print ("Your score is "+ str(score) + " now")
        else:
            print("Nope")
         
    else:
        print(interested + "?  Maybe next time!")
        quit()
        
    

main()


