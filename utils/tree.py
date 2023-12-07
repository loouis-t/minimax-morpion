"""
Module pour la classe Tree utilisée dans le jeu.

Ce module contient la classe Tree qui représente un arbre de jeu. L'arbre de jeu
est utilisé pour stocker tous les mouvements possibles dans le jeu.
"""


class Tree:
    """
    Cette classe représente un arbre de jeu.
    """

    def __init__(self, jeu: list[list[str]]):
        """
        Initialise un nouvel arbre de jeu.

        Args:
            jeu (list[list[str]]): L'état initial du jeu.
        """

        self.jeu = jeu
        self.children: list["Tree"] = []

    def get_jeu(self) -> list[list[str]]:
        """
        Renvoie l'état du jeu à ce noeud.

        Returns:
            list[list[str]]: L'état du jeu à ce noeud.
        """

        return self.jeu

    def add_child(self, child: "Tree"):
        """
        Ajoute un enfant à ce noeud.

        Args:
            child (Tree): L'enfant à ajouter.
        """

        self.children.append(child)

    def get_children(self) -> list["Tree"]:
        """
        Renvoie les enfants de ce noeud.

        Returns:
            list[Tree]: Les enfants de ce noeud.
        """

        return self.children

    def __str__(self, level=0) -> str:
        """
        Renvoie une représentation sous forme de chaîne de l'arbre.

        Returns:
            str: Une représentation sous forme de chaîne de l'arbre.
        """

        ret = "\t" * level + repr(self.jeu) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
