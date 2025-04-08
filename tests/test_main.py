"""Tests for the main module."""

from mypackage.main import hello


def test_hello() -> None:
    """Test the hello function."""
    assert hello() == "Hello, World!"
    assert hello("Python") == "Hello, Python!"
