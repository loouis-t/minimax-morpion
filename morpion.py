from utils.tree import Tree


class Morpion:
    """
    Classe représentant un jeu de Morpion.
    """

    def __init__(
        self,
        jeu: list[list[str]] = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ],
    ):
        """
        Initialise un nouveau jeu de Morpion.
        """

        self.jeu = jeu

        self.tour = False

    def __str__(self) -> str:
        """
        Renvoie une représentation en chaîne de caractères du jeu.
        """

        return (
            f"   0   1   2\n"
            "0  {} | {} | {}\n"
            "  ---+---+---\n"
            "1  {} | {} | {}\n"
            "  ---+---+---\n"
            "2  {} | {} | {}\n"
        ).format(*[case for ligne in self.jeu for case in ligne])

    def jouer(self, joueur: bool, x: int, y: int) -> bool:
        """
        Permet à un joueur de jouer un coup.

        Args:
            joueur (bool): Le joueur qui joue le coup (True ou False).
            x (int): La position x du coup.
            y (int): La position y du coup.

        Returns:
            bool: True si le coup a été joué, False sinon.
        """

        if self.tour == joueur:
            if self.jeu[y][x] == " ":
                self.jeu[y][x] = "X" if not joueur else "O"
                self.tour = True if not joueur else False
                print("played {}, {}".format(x, y))
                if self.is_won():
                    print(f"Joueur {joueur} a gagné")
                return True
            else:
                print("Case déjà prise")
                return False
        else:
            print("Ce n'est pas votre tour")
            return False

    def get_jeu(self) -> list[list[str]]:
        """
        Renvoie l'état actuel du jeu.

        Returns:
            list[list[str]]: L'état actuel du jeu.
        """

        return self.jeu

    def is_won(self) -> bool:
        """
        Vérifie si un joueur a gagné le jeu.

        Args:
            jeu (list): L'état du jeu à vérifier. Si aucun n'est fourni, vérifie
            l'état actuel du jeu.

        Returns:
            bool: True si un joueur a gagné, False sinon.
        """

        # Vérification des lignes
        for ligne in self.jeu:
            if ligne[0] == ligne[1] == ligne[2] != " ":
                return True

        # Vérification des colonnes
        for i in range(3):
            if self.jeu[0][i] == self.jeu[1][i] == self.jeu[2][i] != " ":
                return True

        # Vérification des diagonales
        if self.jeu[0][0] == self.jeu[1][1] == self.jeu[2][2] != " ":
            return True

        if self.jeu[0][2] == self.jeu[1][1] == self.jeu[2][0] != " ":
            return True

        return False

    def has_valid_moves(self) -> bool:
        """
        Checks if there are any valid moves left in the game.

        Returns:
            bool: True if there are valid moves left, False otherwise.
        """
        for row in self.jeu:
            if " " in row:
                return True
        return False

    def generate_moves(self, depth: int = 10) -> "Tree":
        """
        Génère tous les mouvements possibles à partir de l'état actuel du jeu.

        Args:
            depth (int): La profondeur de l'arbre à générer.

        Returns:
            Tree: Un arbre de jeu représentant tous les mouvements possibles.
        """

        # Crée un nouvel arbre avec l'état actuel du jeu
        tree = Tree(self.get_jeu())

        # Si la profondeur est supérieure à 0 et le jeu n'est pas terminé
        if depth > 0 and not self.is_won():
            # Génère tous les mouvements possibles
            for i in range(3):
                for j in range(3):
                    if self.jeu[i][j] == " ":
                        # Crée une copie du jeu
                        jeu = Morpion()
                        jeu.jeu = [ligne.copy() for ligne in self.get_jeu()]
                        jeu.tour = self.tour
                        # Joue le coup
                        if jeu.jouer(self.tour, j, i):
                            # Ajoute le mouvement à l'arbre
                            tree.add_child(jeu.generate_moves(depth - 1))

        return tree

    def heuristic(self, jeu=None) -> int:
        """
        Évalue l'état du jeu.

        Args:
            jeu (list): L'état du jeu à évaluer. Si aucun n'est fourni, évalue
            l'état actuel du jeu.

        Returns:
            int: Le score de l'état du jeu.
        """

        if jeu is None:
            jeu = self.jeu

        # Initialise le score à 0
        score = 0

        # Vérifie les lignes
        for ligne in jeu:
            if ligne.count("X") == 3:
                score += 100
            elif ligne.count("X") == 2 and ligne.count(" ") == 1:
                score += 10
            elif ligne.count("O") == 3:
                score -= 100
            elif ligne.count("O") == 2 and ligne.count(" ") == 1:
                score -= 50  # Increase the penalty for defensive moves

        # Vérifie les colonnes
        for i in range(3):
            colonne = [jeu[j][i] for j in range(3)]
            if colonne.count("X") == 3:
                score += 100
            elif colonne.count("X") == 2 and colonne.count(" ") == 1:
                score += 10
            elif colonne.count("O") == 3:
                score -= 100
            elif colonne.count("O") == 2 and colonne.count(" ") == 1:
                score -= 50  # Increase the penalty for defensive moves

        # Vérifie les diagonales
        diagonale1 = [jeu[i][i] for i in range(3)]
        diagonale2 = [jeu[i][2 - i] for i in range(3)]
        for diagonale in [diagonale1, diagonale2]:
            if diagonale.count("X") == 3:
                score += 100
            elif diagonale.count("X") == 2 and diagonale.count(" ") == 1:
                score += 10
            elif diagonale.count("O") == 3:
                score -= 100
            elif diagonale.count("O") == 2 and diagonale.count(" ") == 1:
                score -= 50  # Increase the penalty for defensive moves

        return score

    def minimax(self, node: Tree, depth: int, maximizing_player: bool) -> int:
        """
        Implémente l'algorithme Minimax pour déterminer le meilleur coup à jouer.

        Args:
            node (Node): Le noeud à partir duquel générer l'arbre de jeu.
            depth (int): La profondeur de l'arbre à générer.
            maximizing_layer (bool): True si le joueur maximise le score, False sinon.

        Returns:
            int: Le score du meilleur coup à jouer.
        """

        if depth == 0 or Morpion(node.get_jeu()).is_won():
            return self.heuristic(node.get_jeu())

        if maximizing_player:
            maxEval = float("-inf")
            for child in node.get_children():
                eval = self.minimax(child, depth - 1, False)
                maxEval = max(maxEval, eval)
            return int(maxEval) if maxEval != float("-inf") else 0
        else:
            minEval = float("inf")
            for child in node.children:
                eval = self.minimax(child, depth - 1, True)
                minEval = min(minEval, eval)
        return int(minEval) if minEval != float("inf") else 0

    def get_move(self, node: Tree) -> tuple[int, int]:
        """
        Renvoie le coup à jouer à partir d'un noeud.

        Args:
            node (Node): Le noeud à partir duquel générer l'arbre de jeu.

        Returns:
            tuple[int, int]: Les coordonnées du meilleur coup à jouer.
        """

        best_score = float("+inf")
        best_move = (-1, -1)

        for child in node.get_children():
            score = self.minimax(child, 10, True)
            if score < best_score:
                best_score = score
                for i in range(3):
                    for j in range(3):
                        if child.get_jeu()[i][j] != self.get_jeu()[i][j]:
                            best_move = (j, i)

        return best_move


# Créer une instance de Morpion
jeu = Morpion()

# Générer l'arbre de jeu
tree = jeu.generate_moves()

# Tant que le jeu n'est pas terminé
while not jeu.is_won() and jeu.has_valid_moves():
    # Afficher le jeu
    print(jeu)

    # Si c'est au tour du joueur
    if not jeu.tour:
        # Demander au joueur de jouer un coup
        x, y = input(
            "Joueur False, entrez les coordonnées de votre coup: "
        ).split()
        while not jeu.jouer(False, int(x), int(y)):
            x, y = input(
                "Joueur False, entrez les coordonnées de votre coup: "
            ).split()
    else:
        # Récupérer le meilleur coup à jouer
        x, y = jeu.get_move(tree)
        # Jouer le coup
        jeu.jouer(True, x, y)

    # get tree child corresponding to the move
    childs = tree.get_children()
    for child in childs:
        print(child.get_jeu())
        if child.get_jeu() == jeu.get_jeu():
            tree = child
            break
    else:
        raise ValueError(
            "No child found with the same game state as the current game."
        )
