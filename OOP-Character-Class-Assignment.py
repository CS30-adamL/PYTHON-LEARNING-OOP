print(" ")
class Character:
    def __init__(character, name, phrase1, phrase2):
        character.name = name
        character.phrase1 = phrase1
        character.phrase2 = phrase2
        character.lvl = 0
        print(f"Character Created: Name:{character.name} Phrase1: {character.phrase1} Phrase2: {character.phrase2} Character level: {character.lvl}\n")

    def speak(character,phraseNum):
        p1_p1 = lambda phraseNum : character.phrase1 if phraseNum == 1 else (character.phrase2 if phraseNum == 2 else 'ERROR')
        print(f"{character.name}: '{p1_p1(phraseNum)}'")

    def setLevel(character, newLevel):
        character.lvl = newLevel
        print(f"{character.name}'s level is now: {character.lvl}")

character1 = Character("Kung Fu Panda","Skadoosh","You have been blinded by pure awesomeness!")
character2 = Character("Spiderman","My Spider-Sense is tingling","Your friendly neighbourhood spiderman.")

character1.speak(1)
character1.setLevel(2)
character1.speak(2)

