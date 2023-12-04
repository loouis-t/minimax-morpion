from utils.node import Node


class Morpion:
    """
    Classe représentant un jeu de Morpion.
    """

    def __init__(self):
        """
        Initialise un nouveau jeu de Morpion.
        """

        self.jeu = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

        self.tour = 0

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

    def jouer(self, joueur: int, x: int, y: int) -> bool:
        """
        Permet à un joueur de jouer un coup.

        Args:
            joueur (int): Le joueur qui joue le coup (0 ou 1).
            x (int): La position x du coup.
            y (int): La position y du coup.

        Returns:
            bool: True si le coup a été joué, False sinon.
        """

        if self.tour == joueur:
            if self.jeu[y][x] == " ":
                self.jeu[y][x] = "X" if joueur == 0 else "O"
                self.tour = 1 if joueur == 0 else 0
                if self.is_won():
                    print(f"Joueur {joueur} a gagné")
                return True
            else:
                print("Case déjà prise")
                return False
        else:
            print("Ce n'est pas votre tour")
            return False

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

    def generate_moves(self) -> list["Morpion"]:
        """
        Génère tous les mouvements possibles à partir de l'état actuel du jeu.

        Returns:
            list[Morpion]: Une liste de nouveaux objets Morpion représentant
            chaque mouvement.
        """

        moves = []
        for i in range(3):
            for j in range(3):
                if self.jeu[i][j] == " ":
                    jeu = Morpion()
                    jeu.jeu = [ligne.copy() for ligne in self.jeu]
                    jeu.jouer(self.tour, j, i)
                    moves.append(jeu)
        return moves

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
            if ligne.count("X") == 2 and ligne.count(" ") == 1:
                score += 10
            elif ligne.count("O") == 2 and ligne.count(" ") == 1:
                score -= 10

        # Vérifie les colonnes
        for i in range(3):
            colonne = [jeu[j][i] for j in range(3)]
            if colonne.count("X") == 2 and colonne.count(" ") == 1:
                score += 10
            elif colonne.count("O") == 2 and colonne.count(" ") == 1:
                score -= 10

        # Vérifie les diagonales
        diagonale1 = [jeu[i][i] for i in range(3)]
        diagonale2 = [jeu[i][2 - i] for i in range(3)]
        for diagonale in [diagonale1, diagonale2]:
            if diagonale.count("X") == 2 and diagonale.count(" ") == 1:
                score += 10
            elif diagonale.count("O") == 2 and diagonale.count(" ") == 1:
                score -= 10

        return score

    def minimax(self, node: Node, depth: int, maximizingPlayer: bool) -> int:
        """
        Implémente l'algorithme Minimax pour déterminer le meilleur coup à jouer.

        Args:
            node (Node): Le noeud à partir duquel générer l'arbre de jeu.
            depth (int): La profondeur de l'arbre à générer.
            maximizingPlayer (bool): True si le joueur maximise le score, False sinon.

        Returns:
            int: Le score du meilleur coup à jouer.
        """

        if depth == 0 or node.get_jeu().is_won():
            return self.heuristic(node.get_jeu())

        if maximizingPlayer:
            maxEval = float("-inf")
            for child in node.get_children():
                eval = self.minimax(child, depth - 1, False)
                maxEval = max(maxEval, eval)
            return int(maxEval)
        else:
            minEval = float("inf")
            for child in node.children:
                eval = self.minimax(child, depth - 1, True)
                minEval = min(minEval, eval)
            return int(minEval)


morpion = Morpion()
print(morpion)
morpion.jouer(0, 1, 1)
print(morpion)
morpion.jouer(1, 2, 1)
print(morpion)
morpion.jouer(0, 1, 0)
print(morpion)
morpion.jouer(1, 2, 2)
print(morpion)
morpion.jouer(0, 1, 2)
print(morpion)
