from abc import ABC
from dataclasses import dataclass

@dataclass
class AbstractCard(ABC):
    name: str
    symbol: str
    module: str
    back: str
