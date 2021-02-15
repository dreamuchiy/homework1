question_answer = {
    "Как дела": "Хорошо",
    "Что делаешь?": "Программурую"
}


def ask_user ():
    print ("Поговори со мной")
    while True:
        try:
            question = input()
            answer = question_answer.get (question)
            print (answer)
        except KeyboardInterrupt:
            print ("Пока!")
            break




ask_user()

