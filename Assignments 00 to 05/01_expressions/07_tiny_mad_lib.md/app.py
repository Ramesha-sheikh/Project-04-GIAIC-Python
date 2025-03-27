SENTENCE_START = "Panaversity is fun. I learned to program and used Python to make my "

def main():
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")

    print(f"{SENTENCE_START}{adjective} {noun} {verb}!")

if __name__ == '__main__':
    main()
