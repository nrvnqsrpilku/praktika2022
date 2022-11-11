def num():
    i = str(input("Введіть першу літеру назви країни = "))
    x = ["460 міст", "110 міст", "30000 міст", "191 міст", "687 міст"]

    if i == "У":
        print(x[0])
    elif i == "Б":
        print(x[1])
    elif i == "С":
        print(x[2])
    elif i == "Е":
        print(x[3])
    elif i == "К":
        print(x[4])
    else:
        print("Такої країни немає у програмі!")

num()
