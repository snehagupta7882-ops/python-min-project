print("----welcome to quiz session----")
quize=[]
while True:
    print("1. ask question")
    print("2. view all questions")
    print("3. view total questions")
    print("4.submit answer")
    print("5.total score")
    print("6.exit")
    choice = int(input("enter your choice:"))
    if choice==1:
        question = input("enter your question:")
        answer = input("enter your answer:")
        quize.append((question, answer))
        print("question added successfully")
    elif choice==2:
        for i in quize:
            print(i)
    elif choice==3:
        print(f"total questions: {len(quize)}")
    elif choice==4:
        score = 0
        for i in quize:
            user_answer = input(f"{i[0]}: ")
            if user_answer.lower() == i[1].lower():
                score += 1
        print(f"your score is: {score}/{len(quize)}")
    elif choice==5:
        print(f"your total score is: {score}/{len(quize)}")
    elif choice==6:
        print("exit")
        break
    else:
        print("invalid choice")