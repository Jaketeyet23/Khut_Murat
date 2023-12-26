def number_to_word(num):

    words = {
        1: "один",
        2: "два",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "восемь",
        9: "деввять",
        10: "десять",
        11: "одиннадцать",
        12: "двенадцать"
    }

    if num < 1 or num > 12:
        return ""

    return words [num]    
if __name__ == "__main__":
    for i in range(1, 13):
        word = number_to_word(1)
        print(f"{i}: {word}")