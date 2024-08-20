# Quiz Program 

quiz = {
    "question1": {
        "question": "What does 'DRY' in python mean?",
        "answer": "don't repeat yourself"
    },

    "question2": {
        "question": "what is 'DYOR' in crypto?",
        "answer": "Do Your Own Research"
    },

    "question3": {
        "question": "Is Vscode an IDE? Yes or No?",
         "answer": "Yes"
    },
   
    "question4": {
        "question": "what is ICP blockchain?",
         "answer": "Internet Computer Protocol"
    },
   
    "question5": {
        "question": "where is FCT in Nigeria?",
         "answer": "Abuja"
    },
   
    "question6": {
        "question": "Is Nigeria in Africa? yes or no? ",
         "answer": "Yes"
    },
   
}

score = 0

for key, value in quiz.items():
    print("")
    print(value['question'])
    answer = input("\nEnter the Answer: \n")

    if answer.lower() == value['answer'].lower():
        print("\nYou are Correct 👌")
        score += 1
        print(f"\nYour Score is: {score}")
        
    elif answer == "":
        print("\nNo Answer inputed! You Scored 0")
        
    else:
        print("You are wrong 👎")
        print(f"\nThe answer is: {value['answer']}")
        print(f"\nYour Score is: {score}")

    
print(f"\nYou got {score} correctly out of 6.")
print(f"\nYou scored {int(score/7 * 100)}%\n")


      




