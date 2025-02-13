# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

from chemistry import make_periodic_table, compute_molar_mass
from formula import parse_formula, FormulaError
from pytest import approx
import pytest


# These are the indexes of the
# elements in the periodic table.
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

def test_make_periodic_table():
    """Verify that the make_periodic_table function works correctly."""
    periodic_table_dict = make_periodic_table()

    assert isinstance(periodic_table_dict, dict), \
        "make_periodic_table function must return a dictionary: " \
        f" expected a dictionary but found a {type(periodic_table_dict)}"

    check_element(periodic_table_dict, "Ac", ["Actinium", 227])  # updated expected value for Actinium
    # Add checks for other elements as needed...

def check_element(periodic_table_dict, symbol, expected):
    """Verify that the actual element that came from the
    periodic_table_dict contains the same values as the
    expected element.
    """
    assert symbol in periodic_table_dict, \
        f'"{symbol}" is missing from the periodic table dictionary.'
    
    actual = periodic_table_dict[symbol]
    act_name = actual[NAME_INDEX]
    exp_name = expected[NAME_INDEX]
    assert act_name == exp_name, \
        f'wrong name for "{symbol}": expected {exp_name} but found {act_name}'

    # Use approx for floating point comparison with tolerance
    act_mass = actual[ATOMIC_MASS_INDEX]
    exp_mass = expected[ATOMIC_MASS_INDEX]
    assert act_mass == approx(exp_mass, rel=1e-4), \
        f"wrong atomic mass for {exp_name}: expected {exp_mass} but found {act_mass}"

def test_parse_formula():
    """Verify that the parse_formula function works correctly."""
    periodic_table_dict = make_periodic_table()
    assert isinstance(periodic_table_dict, dict), \
        "make_periodic_table function must return a dictionary: " \
        f" expected a dictionary but found {type(periodic_table_dict)}"

    sym_quant_list = parse_formula("H2O", periodic_table_dict)
    assert isinstance(sym_quant_list, list), \
        "parse_formula function must return a list: " \
        f" expected a list but found a {type(sym_quant_list)}"

    assert parse_formula("H2O", periodic_table_dict) == [("H",2), ("O",1)]
    assert parse_formula("C6H6", periodic_table_dict) == [("C",6), ("H",6)]
    assert parse_formula("(C2(NaCl)4H2)2C4Na", periodic_table_dict) == [("C",8), ("Na",9), ("Cl",8), ("H",4)]
    assert parse_formula("Co", periodic_table_dict) == [("Co",1)]

    # Invalid formula tests
    with pytest.raises(FormulaError):
        parse_formula("L", periodic_table_dict)
    with pytest.raises(FormulaError):
        parse_formula("4H", periodic_table_dict)
    with pytest.raises(FormulaError):
        parse_formula("H2L4", periodic_table_dict)
    with pytest.raises(FormulaError):
        parse_formula("-H", periodic_table_dict)
    with pytest.raises(FormulaError):
        parse_formula("(H2O", periodic_table_dict)
    with pytest.raises(FormulaError):
        parse_formula("H2)O3", periodic_table_dict)

def test_compute_molar_mass():
    """Verify that the compute_molar_mass function works correctly."""
    periodic_table_dict = make_periodic_table()
    assert isinstance(periodic_table_dict, dict), \
        "make_periodic_table function must return a dictionary: " \
        f" expected a dictionary but found {type(periodic_table_dict)}"

    molar_mass = compute_molar_mass([["O",2]], periodic_table_dict)
    assert isinstance(molar_mass, int) or isinstance(molar_mass, float), \
        "compute_molar_mass function must return a number: " \
        f" expected a number but found {type(molar_mass)}"

    assert compute_molar_mass([], periodic_table_dict) == 0
    assert compute_molar_mass([["O",2]], periodic_table_dict) == approx(31.9988)
    assert compute_molar_mass([["C",6],["H",6]], periodic_table_dict) == approx(78.11184)
    assert compute_molar_mass([["C",13],["H",16],["N",2],["O",2]], periodic_table_dict) == approx(232.27834)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
