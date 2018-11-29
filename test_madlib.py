"""Tests for input/output of madlib.py. Horribly incomplete."""
from madlib import read_file


def test_read_file_exists():
    """Test whether the read_file function exists."""
    assert read_file
