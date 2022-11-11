letter_of_country= str(input("Введіть першу літеру країни:"))
def country(letter_of_country):

    match letter_of_country:
        case "У":
            print("460 міст")
        case "Б":
            print("110 міст")
        case "С":
            print("30000 міст")
        case "Б":
            print("191 міст")
        case "К":
            print("687 міст")
        case _:
            print("Такої країни немає у програмахе!")
        
country(letter_of_country)
