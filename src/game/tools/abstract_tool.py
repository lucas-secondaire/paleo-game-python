from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class AbstractTool(ABC):
    name: str

