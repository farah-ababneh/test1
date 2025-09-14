try:
    with open("test1.txt","r") as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print("test1.txt file is missing.")