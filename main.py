import random

# Liste des mots à trouver pour chaque difficulté
easy_words = ['chat', 'chien', 'lion', 'oiseau', 'lapin', 'souris']
medium_words = ['girafe', 'tortue', 'elephant', 'rhinoceros', 'crocodile', 'hippopotame']
hard_words = ['caméléon', 'ornithorynque', 'okapi', 'kangourou', 'cacatoes', 'pélican']

# Fonction pour générer une grille de lettres aléatoire
def generate_grid(rows, cols):
    # Liste de toutes les lettres possibles
    letters = 'abcdefghijklmnopqrstuvwxyz'
    # Création de la grille vide
    grid = [[' ' for c in range(cols)] for r in range(rows)]
    # Ajout de lettres aléatoires dans chaque case de la grille
    for r in range(rows):
        for c in range(cols):
            grid[r][c] = random.choice(letters)
    return grid

# Fonction pour afficher la grille de lettres
def display_grid(grid):
    for row in grid:
        print(' '.join(row))

# Fonction pour trouver les mots dans la grille
def find_words(grid, words):
    found_words = []
    rows = len(grid)
    cols = len(grid[0])
    # Parcours de chaque mot dans la liste des mots
    for word in words:
        word_found = False
        # Parcours de chaque case de la grille
        for r in range(rows):
            for c in range(cols):
                # Si la première lettre du mot est trouvée dans la case de la grille
                if grid[r][c] == word[0]:
                    # Vérification des lettres suivantes dans les cases voisines
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if dr == dc == 0:
                                continue
                            # Concaténation des lettres voisines pour former un mot potentiel
                            potential_word = grid[r][c]
                            nr, nc = r + dr, c + dc
                            while 0 <= nr < rows and 0 <= nc < cols:
                                potential_word += grid[nr][nc]
                                # Si le mot potentiel correspond au mot cherché
                                if potential_word == word:
                                    found_words.append(word)
                                    word_found = True
                                    break
                                # Sinon, on continue avec les lettres suivantes
                                nr += dr
                                nc += dc
                            if word_found:
                                break
                        if word_found:
                            break
                if word_found:
                    break
    return found_words

# Fonction pour afficher la liste des mots à trouver
def display_words(words):
    print('Mots à trouver:')
    for word in words:
        print('- ' + word)


def main_menu():
    # Affichage du menu
    print('=== Mot mêlé ===')
    print('1. Facile')
    print('2. Moyen')
    print('3. Difficile')
    print('4. Quitter')

    # Initialisation du choix de l'utilisateur
    choice = None

    while choice != '4':
        # Lecture du choix de l'utilisateur
        choice = input('Choisissez une difficulté (1-4): ')

        # Vérification du choix de l'utilisateur
        if choice == '1':
            # Difficulté facile
            grid = generate_grid(5, 10)
            words = easy_words
        elif choice == '2':
            # Difficulté moyenne
            grid = generate_grid(7, 15)
            words = medium_words
        elif choice == '3':
            # Difficulté difficile
            grid = generate_grid(15, 30)
            words = hard_words
        elif choice == '4':
            # Quitter
            return
        else:
            # Choix invalide
            print('Choix invalide. Veuillez choisir une difficulté entre 1 et 4.')
            continue

        # Affichage de la grille de lettres
        print('Grille de lettres:')
        display_grid(grid)

        # Affichage des mots à trouver
        display_words(words)

        # Recherche des mots dans la grille
        found_words = find_words(grid, words)
        # Test
        check_word(grid)
        # Affichage des mots trouvés
        print('Mots trouvés:')
        for word in found_words:
            print('- ' + word)

    # Sortie de la boucle while et fin de la fonction main_menu()
def check_word(grid):
    word = input("Entrez votre mot")
    x1 = int(input("Entrez votre coordonnée x1"))
    y1 = int(input("Entrez votre coordonnée y1"))
    x2 = int(input("Entrez votre coordonnée x2"))
    y2 = int(input("Entrez votre coordonnée y2"))
    # Si les coordonnées sont valides et correspondent à une case de la grille, on ajoute la lettre de cette case au mot
    if 0 <= x1 < len(grid) and 0 <= y1 < len(grid[0]):
        word += grid[x1][y1]
    else:
        return False
    if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]):
        word += grid[x2][y2]
    else:
        return False
    # On vérifie si le mot ainsi formé est égal à un mot de la liste des mots à trouver
    if word in easy_words + medium_words + hard_words:
        print("Le mot", word, "est présent dans la grille.")
    else:
        print("Le mot", word, "n'est pas présent dans la grille.")

# Lancement du jeu
main_menu()
