# water_flow.py

# Constants
EARTH_ACCELERATION_OF_GRAVITY = 9.8066500  # m/s²
WATER_DENSITY = 998.2000000  # kg/m³
WATER_DYNAMIC_VISCOSITY = 0.0010016  # Pa.s

# Pipe-related constants
PVC_SCHED80_INNER_DIAMETER = 0.28687  # meters
PVC_SCHED80_FRICTION_FACTOR = 0.013  # unitless
SUPPLY_VELOCITY = 1.65  # meters/second

HDPE_SDR11_INNER_DIAMETER = 0.048692  # meters
HDPE_SDR11_FRICTION_FACTOR = 0.018  # unitless
HOUSEHOLD_VELOCITY = 1.75  # meters/second

# Function to calculate pressure loss from fittings
def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    P = -0.04 * WATER_DENSITY * fluid_velocity**2 * quantity_fittings / 2000
    return P

# Function to calculate Reynolds number
def reynolds_number(hydraulic_diameter, fluid_velocity):
    R = (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY
    return R

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    if reynolds_number == 0:
        return 0  # Return 0 pressure loss if Reynolds number is 0 (no flow)
    
    k = 0.1 + (50 / reynolds_number) * (larger_diameter / smaller_diameter)**4 - 1
    P = -k * 998.2 * fluid_velocity**2 / 2000
    return P



# Function to convert kPa to psi
def kPa_to_psi(kPa):
    return kPa * 0.145038

# Function to calculate pressure loss from pipe (Darcy-Weisbach equation)
def pressure_loss_from_pipe(diameter, length, friction_factor, velocity):
    # Darcy-Weisbach equation for pressure loss
    P = (friction_factor * length * WATER_DENSITY * velocity**2) / (2 * diameter)
    return P

# Function to calculate water column height
def water_column_height(tower_height, tank_height):
    # Difference in height gives the water column height
    return tower_height - tank_height

# Function to calculate pressure gain from water height
def pressure_gain_from_water_height(water_height):
    # Pressure gain from water column height (in kPa)
    P = WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * water_height / 1000  # Convert to kPa
    return P

# Main function
def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    
    # Calculate water height and pressure
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    
    # Calculate pressure loss in supply pipe
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    
    # Add pressure loss from fittings
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    
    # Calculate pressure loss from pipe reduction
    loss = pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    
    # Change to second pipe diameter and velocity
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    
    # Output pressure in kPa and psi
    print(f"Pressure at house: {pressure:.1f} kilopascals")
    pressure_psi = kPa_to_psi(pressure)
    print(f"Pressure at house: {pressure_psi:.1f} pounds per square inch")

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
