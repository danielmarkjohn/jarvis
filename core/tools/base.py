from abc import ABC, abstractmethod
from typing import Dict, Any, Callable

class BaseTool(ABC):
    """
    Abstract interface enforcing enterprise structure on all Jarvis system capabilities.
    """
    
    @property
    @abstractmethod
    def name(self) -> str:
        """The primary structural identifier namespace for the tool group."""
        pass

    @abstractmethod
    def get_schemas(self) -> list[Dict[str, Any]]:
        """Returns the list of structural JSON schemas to hand off to Ollama."""
        pass

    @abstractmethod
    def get_execution_map(self) -> Dict[str, Callable]:
        """Maps schema string names directly to local Python execution methods."""
        pass