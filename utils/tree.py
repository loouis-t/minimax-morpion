from node import Node


class Tree:
    """
    Classe représentant un arbre de jeu.
    """

    def __init__(self, root: Node):
        """
        Initialise un nouvel arbre avec le noeud racine donné.

        Args:
            root (Node): Le noeud racine de l'arbre.
        """

        self.root = root

    def generate_tree(self, node: Node, depth: int):
        """
        Génère l'arbre de jeu à partir du noeud et de la profondeur donnés.

        Args:
            node (Node): Le noeud à partir duquel générer l'arbre.
            depth (int): La profondeur de l'arbre à générer.
        """

        if depth == 0 or node.jeu.is_won():
            return
        moves = node.jeu.generate_moves()
        for move in moves:
            child = Node(move)
            node.add_child(child)
            self.generate_tree(child, depth - 1)
