from dataclasses import dataclass

from game.cards.abstract_card import AbstractCard

@dataclass
class Character(AbstractCard):
    max_health_points: int
    current_health_points: int
    strength: int
    perception: int
    skill: int
    gift: str
        
    def injure(self, damage_amount: int) -> None:
        self.current_health_points -= damage_amount
        if self.current_health_points <= 0:
            # Mort
            pass
        
    def heal(self, heal_amount: int) -> None:
        self.current_health_points += heal_amount
        self.current_health_points = min(self.max_health_points, self.current_health_points)
        
def create_character(name: str, max_health_points: int, strength: int, perception: int, skill: int, gift: str) -> Character:
    return Character(name, "Footprint", "2", "Character", max_health_points, max_health_points, strength, perception, skill, gift)
        