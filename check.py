import json
data = json.load(open("data.json"))

def translate(w):
    
    return data[w]

word = input("Enter a word: ")

print(translate(word))

#problems if word does not exisits
