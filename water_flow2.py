def water_column_height(tower_height, tank_height):
    """
    Calculate the height of the water column.
    h = t + (3/4) * w
    """
    return tower_height + (3 / 4) * tank_height



def pressure_gain_from_water_height(height):
    """
    Calculate the pressure caused by Earth's gravity pulling on water in an elevated tank.
    P = (ρ * g * h) / 1000
    """
    density = 998.2  # kg/m^3
    gravity = 9.80665  # m/s^2
    return (density * gravity * height) / 1000


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """
    Calculate the water pressure lost due to friction in a pipe.
    P = -(f * L * ρ * v^2) / (2000 * d)
    """
    density = 998.2  # kg/m^3
    if pipe_diameter == 0:  # Prevent division by zero
        raise ValueError("Pipe diameter must be greater than 0.")
    return -(friction_factor * pipe_length * density * fluid_velocity**2) / (2000 * pipe_diameter)
