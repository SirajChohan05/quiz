print("welcome to my computer quiz: ")

playing = input("Do you want to play? ")
score = 0

if playing.lower() == "yes": 
  print("lets play!")

if playing.upper() == "no":
  quit()

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct")
    score +=1
else:
    print("incorrect answer is central processing unit")

answer2 = input("What does RAM stand for: ")
if answer2.lower() == "Random Access Memory":
  print("correct you got 1 point")
  score +=1
else:
  print("The answer is incorrect it is Random Access Memory")
  

print("You got " + str(score) + "questions correct")
print("You got " + str(score/1 * 100) + "%.")

# this can be done for all questions 

# key functions used like .lower and str other things in the code













  

