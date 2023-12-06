class Tree:
    """
    Classe représentant un arbre de jeu.
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
        Returns a string representation of the tree.

        Returns:
            str: A string representation of the tree.
        """
        ret = "\t" * level + repr(self.jeu) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
