from classes import Human, Computer, Game
import json

def read_json(filename):
    try:
        with open(f"{filename}.json", 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Το αρχείο '{filename}.json' δεν υπάρχει.")
        return None

def display_scores(filename):
    best_scores = read_json(filename)
    if best_scores:
        if isinstance(best_scores, list):
            sorted_data = sorted(best_scores, key=lambda x: x['Σκορ'], reverse=True)
            print("\n**** ΤΑ ΚΑΛΥΤΕΡΑ ΣΚΟΡ ****")
            for rank, winner in enumerate(sorted_data, start=1):
                print(f"{rank}. {winner['Νικητής']} - Score: {winner['Σκορ']}")
        else:
            print(f"1. {best_scores['Νικητής']} - Σκορ: {best_scores['Σκορ']}")



# ΡΥΘΜΙΣΕΙΣ ΠΑΙΧΝΙΔΙΟΥ #
user_option = ""
user_name1 = "Παίκτης1"
user_name2 = "Παίκτης2"
difficulty = '3'
filename = "best_scores"


# ΑΡΧΙΚΟ ΜΕΝΟΥ #
while user_option != 'q':
    print("***** SCRABBLE *****")
    print("-" * 10)
    print("1: Νέο Παιχνίδι με Υπολογιστή")
    print("2: Νέο Παιχνίδι για Δύο Άτομα")
    print("3: Ρυθμίσεις")
    print("4: Προβολή Σκορ")
    print("q: Έξοδος")
    print("-" * 10)

    user_option = input()
    if user_option == '1':
        game = Game(Human(user_name1), Computer("Η\Υ", difficulty), 'greek7.txt')
        game.setup()
        game.run()
    elif user_option == '2':
        game = Game(Human(user_name1), Human(user_name2), 'greek7.txt')
        game.setup()
        game.run()
    elif user_option == '3':
        print("***** ΡΥΘΜΙΣΕΙΣ *****")
        print("-" * 10)
        print("1: Αλλαγή username Παίκτη1")
        print("2: Αλλαγή username Παίκτη2")
        print("3: Επιλογή Δυσκολίας Υπολογιστή")
        print("4: Άκυρο")
        print("-" * 10)
        user_option = input()
        if user_option == '1':
            user_name1 = input("Εισάγετε νέο username για τον Παίκτη1: ")
        elif user_option == '2':
            user_name2 = input("Εισάγετε νέο username για τον Παίκτη2: ")
        elif user_option == '3':
            print("***** ΔΥΣΚΟΛΙΑ *****")
            print("-" * 10)
            print("1: Εύκολο (MIN algorithm)")
            print("2: Μέτριο (MAX algorithm)")
            print("3: Δύσκολο (SMART algorithm)")
            print("4: Άκυρο")
            print("-" * 10)
            user_option = input("Επιλέξτε δυσκολία Υπολογιστή (1, 2, 3): ")
            if user_option == '1':
                difficulty = '1'
                print("Επιλέχθηκε Εύκολο.")
            elif user_option == '2':
                difficulty = '2'
                print("Επιλέχθηκε Mέτριο.")
            elif user_option == '3':
                difficulty = '3'
                print("Επιλέχθηκε Δύσκολο.")
            elif user_option != '4':
                print("Λάθος είσοδος. Παρακαλώ πληκτρολόγησε 1, 2, 3 ή 4.")
    elif user_option == '4':
        display_scores(filename)
        input("Enter για Συνέχεια")

print("Έξοδος Προγράμματος...")



