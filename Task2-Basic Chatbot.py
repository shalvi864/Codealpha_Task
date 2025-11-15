#question:answer

qna = {
    "hello":"Hi",
    "how are you":"I'm fine",
    "bye":"Goodbye"
}

while True:
    qs = input()

    if(qs == "quit"):
        break

    else:
        print(qna[qs])