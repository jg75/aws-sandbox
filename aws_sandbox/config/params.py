from abc import ABC
from typing import Any


class Params(ABC):
    """Abstract base class for parameters."""

    vpc: dict[str, Any]

    def __init__(self) -> None:
        """Initialize the Params."""
        pass

    def __str__(self) -> str:
        """Return a string representation of the Params."""
        return self.__class__.__name__

    def __repr__(self) -> str:
        """Return a string representation of the Params."""
        return f"{self.__class__.__name__}()"
