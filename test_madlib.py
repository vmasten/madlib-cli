"""Tests for input/output of madlib.py."""
import madlib
import pytest
import sys


def test_read_file_exists():
    """Test whether the read_file function exists."""
    assert madlib.read_file


def test_write_file():
    """Test whether write_file works properly."""
    madlib.write_file('./foo.txt', 'foo')

    with open('./foo.txt') as f:
        assert f.read() == 'foo'


def test_get_keys():
    """Tests whether get_keys can get parts of speech from simple input."""
    raw = 'It was a {Adjective} and {Adjective} {Noun}'
    expected = ['Adjective', 'Adjective', 'Noun']
    assert madlib.get_keys(raw) == expected


def test_remove_keys():
    """Tests the removal of keys from a given string."""
    raw = 'It was a {Adjective} and {Adjective} {Noun}'
    expected = 'It was a {} and {} {}'
    assert madlib.remove_keys(raw) == expected


def test_parse():
    """Test whether parse works with simple input."""
    prompts, stripped = madlib.parse('It was a {Adjective} and {Adjective} {Noun}')
    assert prompts == ['Adjective', 'Adjective', 'Noun']
    assert stripped == 'It was a {} and {} {}'


def test_output_story():
    """Test whether story output is well-formed."""

    raw = 'It was a {Adjective} and {Adjective} {Noun}'

    input_values = iter(['dark', 'stormy', 'night'])

    def mock_input(s):
        return next(input_values)

    madlib.input = mock_input

    story = madlib.output_story(raw)

    assert story == 'It was a dark and stormy night'
