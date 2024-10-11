import random
import itertools
import json



            
def guidelines():
    """
    1. Κλάσεις:
    - SakClass: Αναπαριστά ένα σακουλάκι με γράμματα για το παιχνίδι σκραμπλ.
    - Player: Βασική κλάση παίκτη.
    - Human: Υποκλάση της κλάσης Player για τον ανθρώπινο παίκτη.
    - Computer: Υποκλάση της κλάσης Player για τον υπολογιστή.
    - Game: Αναπαριστά ένα παιχνίδι Scrabble μεταξύ δύο παικτών.

    2. Κληρονομικότητα:
    - Η κλάση Player είναι η βασική κλάση για τους παίκτες.
    - Οι κλάσεις Human και Computer κληρονομούν από την κλάση Player.

    3. Επέκταση Μεθόδων:
    - Η κλάση Human επεκτείνει την ανώτερη κλάση Player με τις μεθόδους play() και reset_generator().
    - Η κλάση Computer επεκτείνει την ανώτερη κλάση Player με τις μεθόδους play(), calculate_score(), min_algorithm(), max_algorithm(), smart_algorithm() και reset_generator().

    4. Χρησιμοποιήθηκαν τα εξής decorators:
    - word_in_dictionary: Ελέγχει αν η λέξη που δόθηκε από τον παίκτη υπάρχει στο λεξικό της γλώσσας. Αν όχι, εμφανίζει ένα μήνυμα στον ανθρώπινο παίκτη και τον καλεί να δώσει μια νέα λέξη.
       
    - is_playable: Ελέγχει αν ο παίκτης έχει τα απαραίτητα γράμματα για να σχηματίσει την επιλεγμένη λέξη. Αν όχι, εμφανίζει ένα μήνυμα στον ανθρώπινο παίκτη και τον καλεί να δώσει μια νέα λέξη.

    5. Η εφαρμογή οργανώνει τις λέξεις της γλώσσας σε ένα λεξικό (dictionary) κατά τη διάρκεια του παιχνιδιού.

    6. Υλοποιήθηκαν οι ακόλουθοι αλγόριθμοι για τον υπολογιστή παίκτη:
    -max: επιλέγει λέξεις από τα γράμματα του παίκτη, ξεκινώντας από τις μεγαλύτερες δυνατές λέξεις.
    -min: επιλέγει λέξεις από τα γράμματα του παίκτη, ξεκινώντας από τις μικρότερες δυνατές λέξεις.
    -smart: επιλέγει λέξεις με βάση την μέγιστη βαθμολογία.
    """

class SakClass:   
    def __init__(self):
        self.letters = []

    def __repr__(self):
        return f"Γράμματα στο σακί: {self.letters_remaining()}"


    def randomize_sak(self):
        self.letters = (
            ['Α'] * 12 +
            ['Β'] * 1 +
            ['Γ'] * 2 +
            ['Δ'] * 2 +
            ['Ε'] * 8 +
            ['Ζ'] * 1 +
            ['Η'] * 7 +
            ['Θ'] * 1 +
            ['Ι'] * 8 +
            ['Κ'] * 4 +
            ['Λ'] * 1 +
            ['Μ'] * 4 +
            ['Ν'] * 6 +
            ['Ξ'] * 1 +
            ['Ο'] * 9 +
            ['Π'] * 4 +
            ['Ρ'] * 4 +
            ['Σ'] * 7 +
            ['Τ'] * 8 +
            ['Υ'] * 4 +
            ['Φ'] * 1 +
            ['Χ'] * 1 +
            ['Ψ'] * 1 +
            ['Ω'] * 1
        )
        random.shuffle(self.letters)

    def get_letters(self, n):
        if n > len(self.letters):
            n = len(self.letters)
        drawn = self.letters[:n]
        self.letters = self.letters[n:]
        return drawn

    def put_back_letters(self, letters):
        self.letters.extend(letters)


    def letters_remaining(self):
        return len(self.letters)

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.letters = []

    def __repr__(self):
        return f"{self.name} - Σκορ: {self.score}"

    def receive_letters(self, letters):
        self.letters.extend(letters)

    def is_playable(self, word):
        for letter in word:
            if letter not in self.letters:
                return False
        return True

    def place_word(self, word, score):
        for letter in word:
            self.letters.remove(letter)
        self.score += score
    

class Human(Player):
    def play(self):
        return input("ΛΕΞΗ: ").strip().upper()

    def reset_generator(self):
        pass
    

class Computer(Player):
    
    def __init__(self, name, difficulty):
        super().__init__(name)
        self.difficulty = difficulty
        self.points = {
            'Α': 1, 'Β': 8, 'Γ': 4, 'Δ': 4, 'Ε': 1, 'Ζ': 10, 'Η': 1, 'Θ': 10,
            'Ι': 1, 'Κ': 2, 'Λ': 3, 'Μ': 3, 'Ν': 1, 'Ξ': 10, 'Ο': 1, 'Π': 2,
            'Ρ': 2, 'Σ': 1, 'Τ': 1, 'Υ': 2, 'Φ': 8, 'Χ': 8, 'Ψ': 10, 'Ω': 3}

        if difficulty == '1':
            self.generator = self.min_algorithm()
        elif difficulty == '2':
            self.generator = self.max_algorithm()
        elif difficulty == '3':
            self.generator = self.smart_algorithm()

    def play(self):
        try:
            return next(self.generator)
        except StopIteration:
            return 'PASS'

    def min_algorithm(self):
        for length in range(2, 8):
            for perm in itertools.permutations(self.letters, length):
                yield ''.join(perm)

    def max_algorithm(self):
        max_length = 7
        for length in range(max_length, 1, -1):  
            for perm in itertools.permutations(self.letters, length):
                yield ''.join(perm)

    def calculate_score(self, word):
        score = 0
        for letter in word:
            if letter in self.points:
                score += self.points[letter]
        return score

    def smart_algorithm(self):
        words_with_scores = []
        for length in range(7, 1, -1):  # Adjust range based on max word length you want to consider
            for perm in itertools.permutations(self.letters, length):
                word = ''.join(perm)
                score = self.calculate_score(word)
                words_with_scores.append((word, score))
        
        words_with_scores.sort(key=lambda x: x[1], reverse=True)  # Sort by score in descending order
        
        for word, _score in words_with_scores:
            yield word

    def reset_generator(self):
        if self.difficulty == '1':
            self.generator = self.min_algorithm()
        elif self.difficulty == '2':
            self.generator = self.max_algorithm()
        elif self.difficulty == '3':
            self.generator = self.smart_algorithm()

class Game:
    
    def __init__(self, player1, player2, filename):
        self.sak = SakClass()
        self.players = [player2, player1]
        self.turn = 1
        self.filename = filename
        self.my_dictionary = {}
        self.points = {
            'Α': 1, 'Β': 8, 'Γ': 4, 'Δ': 4, 'Ε': 1, 'Ζ': 10, 'Η': 1, 'Θ': 10,
            'Ι': 1, 'Κ': 2, 'Λ': 3, 'Μ': 3, 'Ν': 1, 'Ξ': 10, 'Ο': 1, 'Π': 2,
            'Ρ': 2, 'Σ': 1, 'Τ': 1, 'Υ': 2, 'Φ': 8, 'Χ': 8, 'Ψ': 10, 'Ω': 3}
    
    def __repr__(self):
        player_index = self.turn % len(self.players)
        return "*" * 20 + f"\nΓύρος {self.turn}\n{self.sak.__repr__()} - Παίζει {self.players[player_index].name}"
    
    def load_words(self, filename):
        words = {}
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                word = line.strip()
                words[word] = True
        return words
    
    def word_in_dictionary(self, word_to_check):
        if word_to_check in self.my_dictionary:
            return True
        else:
            return False

    def calculate_score(self, word):
        score = 0
        for letter in word:
            if letter in self.points:
                score += self.points[letter]
        return score
    
    def setup(self):
        self.sak.randomize_sak()
        for player in self.players:
            player.receive_letters(self.sak.get_letters(7))
        self.my_dictionary = self.load_words(self.filename)
    
    def run(self):
        print("**** ΕΚΚΙΝΗΣΗ ΠΑΙΧΝΙΔΙΟΥ ****")
        quit_game = False
        while self.sak.letters_remaining() >= 7 and not quit_game:
            print(self.__repr__())
            player_index = self.turn % len(self.players)
            letters_with_points = [f"({letter},{self.points[letter]})" for letter in self.players[player_index].letters]
            print("Διαθέσιμα Γράμματα: ", end = "")
            print(" - ".join(letters_with_points))
            word = self.players[player_index].play()
            valid_word = False
            while not valid_word:
                if word == 'Q' or word == 'EXIT' or word == 'QUIT':
                    quit_game=True
                    valid_word=True
                elif word == 'P' or word == 'PASS':
                    valid_word=True
                    temp = self.sak.get_letters(7)
                    self.sak.put_back_letters(self.players[player_index].letters)
                    self.players[player_index].letters = temp
                    print(f"Ο {self.players[player_index].name} πήγε πάσο για να αλλάξει τα γράμματά του!")
                elif not self.word_in_dictionary(word):
                    if isinstance(self.players[player_index], Human):
                        print(f"Η λέξη {word} δεν υπάρχει στο λεξικό! Δοκιμάσε ξανα. Για πάσο πάτα 'p'.")
                    word = self.players[player_index].play()
                elif not self.players[player_index].is_playable(word):
                    if isinstance(self.players[player_index], Human):
                        print(f"Δεν έχεις τα γράμματα για να παίξεις την λέξη {word}! Δοκιμάσε ξανα.")
                    word = self.players[player_index].play()
                else:
                    print(f"Ο {self.players[player_index].name} έπαιξε {word}!")
                    valid_word = True
                    self.players[player_index].place_word(word, self.calculate_score(word))
                    self.players[player_index].receive_letters(self.sak.get_letters(len(word)))
                    print(f"Αποδεκτή λέξη - Βαθμοί: {self.calculate_score(word)} - Σκορ: {self.players[player_index].score}")
            input("Enter για Συνέχεια")
            self.players[player_index].reset_generator()
            self.turn += 1
        self.end()

    def end(self):
        scoreboard = [(player, player.score) for player in self.players]
        scoreboard.sort(key=lambda x: x[1], reverse=True)
        print()
        print("****ΤΕΛΟΣ ΠΑΙΧΝΙΔΙΟΥ****")
        for rank, (player, score) in enumerate(scoreboard, start=1):
            print(f"{rank}. {player.__repr__()}")
        print()
        print(f"Νικητής ο {scoreboard[0][0].name} !!")
        print()

        winner_data = {
            "Νικητής": scoreboard[0][0].name,
            "Σκορ": scoreboard[0][1]
        }

        try:
            # Open the JSON file if it exists
            with open('best_scores.json', 'r+', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    # Check if the data is a list
                    if isinstance(data, list):
                        data.append(winner_data)
                    else:
                        data = [data, winner_data]
                except json.JSONDecodeError:
                    # If the file is empty or not a valid JSON, start with a new list
                    data = [winner_data]
                # Move the file pointer to the beginning and truncate the file
                f.seek(0)
                f.truncate()
                # Write the updated data back to the file
                json.dump(data, f, ensure_ascii=False, indent=4)
        except FileNotFoundError:
            # If the file does not exist, create it and write the winner data
            with open('best_scores.json', 'w', encoding='utf-8') as f:
                json.dump([winner_data], f, ensure_ascii=False, indent=4)



