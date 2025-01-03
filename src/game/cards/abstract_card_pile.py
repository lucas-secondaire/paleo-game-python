import random
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

from game.cards.abstract_card import AbstractCard

@dataclass
class AbstractCardPile(ABC):
    name: str
    cards: List[AbstractCard]
        
    def add_card(self, card: AbstractCard) -> None:
        self.cards.append(card)
        
    def draw_card(self) -> AbstractCard | None:
        if len(self.cards) != 0:
            return self.cards.pop(0)
        else:
            return None
        
    def remove_card(self, index: int) -> None:
        if len(self.cards) >= index + 1:
            self.cards.pop(index)
        
    def shuffle_card_pile(self) -> None:
        random.shuffle(self.cards)
        
    def display_card_backs(self) -> None:
        for card in self.cards:
            print(card.back)