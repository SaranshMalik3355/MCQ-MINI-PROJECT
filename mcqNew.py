import random
import time

def geo_quiz():
        ques_lst = [
                        "What is the capital of Australia?",
                        "Which is the longest river in the world?",
                        "Mount Everest is located in which mountain range?",
                        "Which desert is the largest in the world?",
                        "Which country has the largest population in the world?"
                    ]
        option_lst = [
                        ["A) Sydney", "B) Melbourne", "C) Canberra", "D) Brisbane"],
                        ["A) Amazon River", "B) Nile River", "C) Yangtze River", "D) Mississippi River"],
                        ["A) Andes", "B) Alps", "C) Himalayas", "D) Rockies"],
                        ["A) Sahara Desert", "B) Arabian Desert", "C) Gobi Desert", "D) Antarctic Desert"],
                        ["A) USA", "B) India", "C) China", "D) Indonesia"]
                    ]
        correct_answers = ["C", "B", "C", "D", "B"]
        return answer_checker(ques_lst, option_lst, correct_answers)
        

    
#-------------- Math quiz ----------------

def maths_quiz():
        ques_lst = [
                        "What is 15 'x' 6?",
                        "What is the square root of 144?",
                        "What is 25'%' of 200?",
                        "What is 9²?",
                        "What is 100 divided by 4?"
                    ]
        option_lst = [
                        ["A) 90", "B) 80", "C) 85", "D) 95"],
                        ["A) 10", "B) 11", "C) 12", "D) 14"],
                        ["A) 40", "B) 45", "C) 50", "D) 55"],
                        ["A) 72", "B) 81", "C) 99", "D) 64"],
                        ["A) 20", "B) 25", "C) 30", "D) 40"]
                        
                    ]
        correct_answers = ["A", "C", "C", "B", "B"]
        return answer_checker(ques_lst, option_lst, correct_answers)

        
        
#-------------- sceince quiz ----------------

def science_quiz():
    # while True:
        ques_lst = [
                        "What planet is known as the Red Planet?",
                        "What gas do humans need to breathe?",
                        "What is the chemical symbol for water?",
                        "Which organ pumps blood in the human body?",
                        "What force pulls objects toward Earth?"
                    ]
        option_lst = [
                        ["A) Indian Ocean", "B) Atlantic Ocean", "C) Pacific Ocean", "D) Arctic Ocean"],
                        ["A) Queue", "B) Stack", "C) Tree", "D) Graph"],
                        ["A) China", "B) Japan", "C) Thailand", "D) South Korea"],
                        ["A) Alan Turing", "B) Charles Babbage", "C) Bill Gates", "D) Steve Jobs"],
                        ["A) Oxygen", "B) Nitrogen", "C) Carbon Dioxide", "D) Hydrogen"]
                        
                    ]
        correct_answers = ["B", "C", "A", "C", "B"]
        return answer_checker(ques_lst, option_lst, correct_answers)
         
    
    
#Answer func
   
def answer_checker(ques_lst, option_lst, correct_answers):
        score = 0
        no_of_correct = 0
        index_lst = list(range(len(ques_lst)))
        total_questions = len(ques_lst)
        random.shuffle(index_lst)
        start = time.time()
        for  position,value in enumerate(index_lst):
            # print(ques_lst[index_lst[i]])
            print(f"Question {position + 1}: \n{ques_lst[value]}")
            for k in option_lst[value]:
                print(f"{k}")
            while True: 
                solution = input("Enter the answer: ").strip().capitalize()
                if solution not in ["A", "B", "C", "D"]:
                    print("You have entered an invalid input. Please enter the answer again")
                elif solution == correct_answers[value]:
                    print("Correct answer")
                    no_of_correct += 1
                    score += 10
                    break
                else:
                    print(f"Wrong answer. The correct option is {correct_answers[value]}")
                    score -= 5
                    break
        end = time.time()
        length = end - start
        print("You took", length, "seconds!")
        print(f"Your final score is {score}.")
        # print(f"Your total score is {total_score}.")
        print(f"The total number of correct answers you gave is {no_of_correct} out of {total_questions}.")
        return score

def main():
    geo_score = 0
    math_score = 0
    science_score = 0
    while True: 
        try: 
            user_choice = int(input("Please enter 1. To take geography quiz \nPlease enter 2. To take maths quiz \nPlease enter 3. To take science quiz:\nOr enter 0 to Exit: \n")) 
            
            if user_choice not in [0,1,2,3]: 
                print("You have entered wrong number please select from given number only") 
                continue 
        
            if user_choice == 1: 
               geo_score = geo_quiz()
            elif user_choice == 2:
                math_score = maths_quiz() 
            elif user_choice == 3:
                science_score = science_quiz()
            else: 
                print(f"You choose to exit. Exiting the app")
                break 
            
        except ValueError: 
            print("Enter only valid number, no string") 
    
        
    consolidated_score = geo_score + math_score + science_score
    print("\n------ Quiz Summary ------")
    print(f"Geography Score : {geo_score}")
    print(f"Maths Score     : {math_score}")
    print(f"Science Score   : {science_score}")
    print("--------------------------")
    print(f"Total Score     : {consolidated_score}")
            
            
main()


            
        