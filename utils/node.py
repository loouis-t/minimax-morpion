from morpion import Morpion


class Node:
    """
    Classe représentant un noeud dans l'arbre de jeu.
    """

    def __init__(self, jeu: Morpion):
        """
        Initialise un nouveau noeud avec le jeu donné.

        Args:
            jeu (Morpion): L'état du jeu à ce noeud.
        """

        self.jeu = jeu
        self.children: list["Node"] = []

    def get_jeu(self) -> Morpion:
        """
        Renvoie l'état du jeu à ce noeud.

        Returns:
            Morpion: L'état du jeu à ce noeud.
        """

        return self.jeu

    def get_children(self) -> list["Node"]:
        """
        Renvoie les enfants de ce noeud.

        Returns:
            list[Morpion]: Les enfants de ce noeud.
        """

        return self.children

    def add_child(self, child: "Node"):
        """
        Ajoute un enfant à ce noeud.

        Args:
            child (Morpion): L'enfant à ajouter.
        """

        self.children.append(child)
