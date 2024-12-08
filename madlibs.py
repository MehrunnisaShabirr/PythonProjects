def greet():
    print('''Hello
    Welcome to Matlib Game
    **********************
    ''')


def create_story():
    adjective = input("Enter any adjective:\n")
    verb = input("Enter a verb:\n")
    place = input("Enter your favourite place:\n")
    thing = input("Enter the name of any object:\n")
    noun = input("Enter any noun:\n")
    animal = input("Enter the name of your favorite animal:\n")
    food = input("Enter the name of any food you want to eat right now:\n")

    print(f'''Once upon a time, in the {adjective} land of {place}, there was a brave hero named {noun}.
    One day, while {noun} was {verb} through the forest, they stumbled upon a {thing}.
    Suddenly, a {animal} appeared out of nowhere, guarding a magical {food}.
    With a determined heart, {noun} set out on an epic quest to tame the {animal} and claim the enchanted {food}.
    The journey through {place} was filled with danger, but {noun}'s courage and wit saw them through!''')

greet()
create_story()