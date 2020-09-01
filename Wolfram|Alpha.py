import wolframalpha

input = input("Question:")
app_id = "5AUQ5Y-7E7U4H4TUL" #id that should be generated
client = wolframalpha.Client(app_id)

res = client.query(input)
answer = next(res.results).text

print(answer)
