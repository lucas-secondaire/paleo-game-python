from dataclasses import dataclass
from typing import Any, List

from game.cards.character import Character

@dataclass
class Game:
    modules: List[str]
    characters: List[Character]
    group: List[Any]
    meats: int = 0
    woods: int = 0
    stones: int = 0
    mammoth_tokens: int = 0
    skull_tokens: int = 0
    
    actions_pile = []
    characters_pile = []
    dreams_pile = []
    ideas_pile = []
    secrets = []
    missions = []
    
    def get_action_cards(self):
        pass
    
    def draw_two_characters(self):
        pass
    
    def get_mission_cards(self):
        pass
        
    def verify_end_condition(self) -> None:
        if self.mammoth_tokens >= 5:
            print("WIN")
        elif self.skull_tokens >= 5:
            print("LOSE")
        else:
            print("MENFOU")
    