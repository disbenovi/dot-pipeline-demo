"""Greeting strings. Deliberately tiny — the demo needs something to change."""

DEFAULT_NAME = "world"


def greet(name: str = DEFAULT_NAME) -> str:
    """Return a greeting for ``name``."""
    name = (name or "").strip() or DEFAULT_NAME
    return f"Hello, {name}!"


def farewell(name: str = DEFAULT_NAME) -> str:
    """Return a farewell for ``name``."""
    name = (name or "").strip() or DEFAULT_NAME
    return f"Goodbye, {name}."
