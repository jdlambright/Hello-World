from question import Question

question_prompts = [
    "what kind of dog is Nolee? \na) A wolf \nb) A chiwahwa \nc) A golden doodle\n\n",
    "what is Nora's favorite animal? \na) A wolf \nb) A unicorn \nc) A pig\n\n",
    "what is Owen's favorite animal? \na) A dinosaur \nb) A cow \nc) A walrus\n\n"
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + " out of " + str(len(questions)) + " correct!!!")
    if score > 1:
        print("great job!")
    else:
        print("Better luck next time!!")

run_test(questions)