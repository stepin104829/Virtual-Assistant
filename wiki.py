import wikipedia


while True:
    input_wiki = input("Question: ")
    ans = (wikipedia.summary(input_wiki))
    print(ans)
