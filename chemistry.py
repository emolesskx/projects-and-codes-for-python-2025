# Importing the parse_formula function from the formula.py file
from formula import parse_formula

# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1
ATOMIC_NUMBER_INDEX = 2  # Atomic number (protons)

# Function to make the periodic table
def make_periodic_table():
    """Create and return a dictionary representing the periodic table."""
    periodic_table_dict = {
        "H": ["Hydrogen", 1.00794, 1],
        "He": ["Helium", 4.002602, 2],
        "Li": ["Lithium", 6.941, 3],
        "Be": ["Beryllium", 9.0122, 4],
        "B": ["Boron", 10.81, 5],
        "C": ["Carbon", 12.0107, 6],
        "N": ["Nitrogen", 14.0067, 7],
        "O": ["Oxygen", 15.9994, 8],
        "F": ["Fluorine", 18.9984032, 9],
        "Ne": ["Neon", 20.1797, 10],
        "Ac": ["Actinium", 227.0278, 89],  # Added Actinium (Ac)
        # Add other elements as needed
    }
    return periodic_table_dict

# Function to compute molar mass
def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the elements in the list."""
    total_molar_mass = 0
    for element, quantity in symbol_quantity_list:
        atomic_mass = periodic_table_dict[element][ATOMIC_MASS_INDEX]
        total_molar_mass += atomic_mass * quantity
    return total_molar_mass

# Function to compute the total number of protons
def sum_protons(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total number of protons in all the elements."""
    total_protons = 0
    for element, quantity in symbol_quantity_list:
        atomic_number = periodic_table_dict[element][ATOMIC_NUMBER_INDEX]
        total_protons += atomic_number * quantity
    return total_protons

# Function to return the compound name based on the formula
def get_formula_name(formula, known_molecules_dict):
    """Try to find formula in the known_molecules_dict.
    If formula is in the known_molecules_dict, return
    the name of the chemical formula; otherwise return
    "unknown compound".
    """
    return known_molecules_dict.get(formula, "unknown compound")

# Main function to drive the program
def main():
    # Dictionary of known chemical formulas and their names
    known_molecules_dict = {
        "Al2O3": "aluminum oxide",
        "CH3OH": "methanol",
        "C2H6O": "ethanol",
        "C2H5OH": "ethanol",
        "C3H8O": "isopropyl alcohol",
        "C3H8": "propane",
        "C4H10": "butane",
        "C6H6": "benzene",
        "C6H14": "hexane",
        "C8H18": "octane",
        "CH3(CH2)6CH3": "octane",
        "C13H18O2": "ibuprofen",
        "C13H16N2O2": "melatonin",
        "Fe2O3": "iron oxide",
        "FeS2": "iron pyrite",
        "H2O": "water"
    }

    # Get user input
    formula = input("Enter the molecular formula of the sample: ")
    mass = float(input("Enter the mass in grams of the sample: "))
    
    # Convert the formula to uppercase to handle case sensitivity (important for parsing)
    formula = formula.upper()
    
    # Get the periodic table
    periodic_table_dict = make_periodic_table()
    
    # Parse the formula and pass the periodic table dictionary as the second argument
    try:
        symbol_quantity_list = parse_formula(formula, periodic_table_dict)
    except Exception as e:
        print(f"Formula parsing error: {e}")
        return
    
    # Compute the molar mass
    molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table_dict)
    
    # Compute the number of moles
    number_of_moles = mass / molar_mass
    
    # Get the compound name from the known molecules dictionary
    compound_name = get_formula_name(formula, known_molecules_dict)
    
    # Compute the total number of protons
    protons = sum_protons(symbol_quantity_list, periodic_table_dict)
    
    # Print the results
    print(f"Compound Name: {compound_name}")
    print(f"{molar_mass:.5f} grams/mole")
    print(f"{number_of_moles:.5f} moles")
    print(f"Total protons: {protons}")

# Run the main function
if __name__ == "__main__":
    main()
