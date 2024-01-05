def MoodFormula(L, M, S):
    happyOrSad = 1 * S + 2 * M + 3 * L
    His_mood=""
    if happyOrSad >= 10:
        His_mood = "Happy"
    elif happyOrSad < 10:
        His_mood = "Sad"
    return His_mood

#Main
def main():
    #input of Small treats
    smallTreats = int(input("Small treats: ").strip())
    #input of Medium treats
    mediumTreats = int(input("Medium treats: ").strip())
    #input of large treats
    largeTreats = int(input("Large treats: ").strip())

    mood = MoodFormula(largeTreats, mediumTreats, smallTreats)
    print(mood)



if __name__ == "__main__":
    main()