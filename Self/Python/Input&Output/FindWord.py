word = "Python"
with open("Chatgpt.txt") as f:
    data = f.read()
    if (data.find(word) != -1):
        print("Found")
    else:
        print("Not Found")
