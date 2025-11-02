"""
Unit tests for the add function
"""
import pytest
from main import add


def test_adds_2_plus_2_equals_4():
    """Test that 2 + 2 equals 4"""
    assert add(2, 2) == 4


def test_adds_negative_numbers():
    """Test addition with negative numbers"""
    assert add(-1, -1) == -2


def test_adds_zero():
    """Test addition with zero"""
    assert add(5, 0) == 5
    assert add(0, 5) == 5


def test_adds_large_numbers():
    """Test addition with large numbers"""
    assert add(1000000, 2000000) == 3000000
