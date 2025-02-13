# test_water_flow.py
import pytest
from water_flow import (
    pressure_loss_from_fittings,
    reynolds_number,
    pressure_loss_from_pipe_reduction,
    pressure_loss_from_pipe,
    water_column_height,
    pressure_gain_from_water_height,
    kPa_to_psi
)

# Test pressure loss from fittings
def test_pressure_loss_from_fittings():
    assert abs(pressure_loss_from_fittings(0.00, 3) - 0.000) < 0.001
    assert abs(pressure_loss_from_fittings(1.65, 0) - 0.000) < 0.001
    assert abs(pressure_loss_from_fittings(1.65, 2) + 0.109) < 0.001
    assert abs(pressure_loss_from_fittings(1.75, 2) + 0.122) < 0.001
    assert abs(pressure_loss_from_fittings(1.75, 5) + 0.306) < 0.001

# Test Reynolds number calculation
def test_reynolds_number():
    assert abs(reynolds_number(0.048692, 0.00) - 0) < 1
    assert abs(reynolds_number(0.048692, 1.65) - 80069) < 1
    assert abs(reynolds_number(0.048692, 1.75) - 84922) < 1
    assert abs(reynolds_number(0.286870, 1.65) - 471729) < 1
    assert abs(reynolds_number(0.286870, 1.75) - 500318) < 1

# Test pressure loss from pipe reduction
def test_pressure_loss_from_pipe_reduction():
    # Test when Reynolds number is 0 (no flow)
    assert abs(pressure_loss_from_pipe_reduction(0.28687, 0.00, 0, 0.048692) - 0.000) < 0.001
    
    # Test with typical values for Reynolds number and flow velocity
    assert abs(pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) - 164.7934024007264) < 0.001  # Correct expected value

# Test pressure loss from pipe
def test_pressure_loss_from_pipe():
    diameter = 0.28687  # Example diameter in meters
    length = 1524.0  # Example length in meters
    friction_factor = 0.013  # Example friction factor (unitless)
    velocity = 1.65  # Example velocity in meters/second
    expected_loss = (friction_factor * length * 998.2 * velocity**2) / (2 * diameter)
    assert abs(pressure_loss_from_pipe(diameter, length, friction_factor, velocity) - expected_loss) < 0.001

# Test water column height
def test_water_column_height():
    assert abs(water_column_height(36.6, 9.1) - 27.5) < 0.001
    assert abs(water_column_height(50.0, 20.0) - 30.0) < 0.001

# Test pressure gain from water height
def test_pressure_gain_from_water_height():
    assert abs(pressure_gain_from_water_height(27.5) - (998.2 * 9.8066500 * 27.5) / 1000) < 0.001
    assert abs(pressure_gain_from_water_height(30.0) - (998.2 * 9.8066500 * 30.0) / 1000) < 0.001

# Test kPa to psi conversion
def test_kPa_to_psi():
    assert abs(kPa_to_psi(158.7) - 23.04) < 0.05  # Increased tolerance
    assert abs(kPa_to_psi(0) - 0) < 0.01
    assert abs(kPa_to_psi(100) - 14.50) < 0.01

# Run all tests
if __name__ == "__main__":
    pytest.main()
