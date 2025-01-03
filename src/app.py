# Pour lancer le jeu
from game.cards.character import Character, create_character

char = create_character("Beau gosse", 3, 1, 0, 0, "Poêle")

import pydoc

text = "Ligne 1\n" + "\n".join(f"Ligne {i}" for i in range(2, 101))  # Texte volumineux
pydoc.pager(text)