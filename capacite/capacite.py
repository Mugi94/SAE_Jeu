from __future__ import annotations
from abc import ABC, abstractmethod

class Capacite(ABC):
    """Interface Capacite"""

    @abstractmethod
    def utiliser(self, personnage, cible):
        pass