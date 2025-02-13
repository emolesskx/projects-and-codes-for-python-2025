"""Verify that the prefix and suffix functions work correctly."""

from words import prefix, suffix
import pytest

def test_suffix():
    # Test cases for the suffix function
    assert suffix("", "") == ""             # Both strings empty
    assert suffix("", "correct") == ""      # First string empty
    assert suffix("clear", "") == ""        # Second string empty
    assert suffix("angelic", "awesome") == ""  # No common suffix
    assert suffix("found", "profound") == "found"  # Common suffix: "found"
    assert suffix("ditch", "itch") == "itch"      # Common suffix: "itch"
    assert suffix("happy", "funny") == "y"        # Common suffix: "y"
    assert suffix("tired", "fatigued") == "ed"    # Common suffix: "ed"
    assert suffix("swimming", "FLYING") == "ing"  # Common suffix: "ing"

# Run the test function
test_suffix()


def test_prefix():
    """Verify that the prefix function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the prefix function and verify that it returns a string.
    pre = prefix("upbeat", "upgrade")
    assert isinstance(pre, str), "prefix function must return a string"

    # Call the prefix function ten times and use an assert
    # statement to verify that the string returned by the
    # prefix function is correct each time.
    assert prefix("cat", "catalog") == "cat"
    assert prefix("", "") == ""
    assert prefix("", "correct") == ""
    assert prefix("clear", "") == ""
    assert prefix("happy", "funny") == ""
    assert prefix("cat", "catalog") == "cat"
    assert prefix("dogmatic", "dog") == "dog"
    assert prefix("jump", "joyous") == "j"
    assert prefix("upbeat", "upgrade") == "up"
    assert prefix("Disable", "dIstasteful") == "dis"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__]) 
