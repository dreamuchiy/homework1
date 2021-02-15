question_answer = {
    "Как дела": "Хорошо",
    "Что делаешь?": "Программурую"
}


def ask_user ():
    print ("Поговори со мной")
    while True:
        question = input()
        answer = question_answer.get (question)
        print (answer)


ask_user()

