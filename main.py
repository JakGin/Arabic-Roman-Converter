import re


roman_arabic = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1
}


def main():
    print("1. Roman to Arabic")
    print("2. Arabic to Roman")
    print("------------------")

    choice = input("Which option: ")

    if choice == "1":
        roman = input("Enter roman number: ")
        print(roman, "=", roman_to_arabic(roman))
    elif choice == '2':
        arabic = input("Enter arabic number: ")
        print(arabic, "=", arabic_to_roman(int(arabic)))
    else:
        print("Invalid option")
    

def validate_roman(number):
    x = re.search("^M{0,3}(CM|CD|D?C{0,3})?(XC|XL|L?X{0,3})?(IX|IV|V?I{0,3})?$", number)
    if not x:
        return False
    else:
        return True


def arabic_to_roman(number):
    if number > 3999 or number <= 0:
        return "Invalid arabic number"

    roman = ""

    for key, value in roman_arabic.items():
        quotient, remainder = divmod(number, value)
        number = remainder
        roman += key * quotient

    return roman


def roman_to_arabic(number):
    if validate_roman(number) == False:
        return "Invalid roman number"

    sum = 0
    previous_sign = "I"

    for sign in reversed(number):
        if roman_arabic[sign] < roman_arabic[previous_sign]:
            sum -= roman_arabic[sign]
        else:
            sum += roman_arabic[sign]
        previous_sign = sign

    return sum


if __name__ == "__main__":
    main()