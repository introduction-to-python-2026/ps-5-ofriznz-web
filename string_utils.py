def split_before_uppercases(formula): 
    split_formula = []
    start = 0
    for end in range(1, len(formula)):
        if formula[end].isupper():
           split_formula.append(formula[start:end])
           start = end 
            
    if formula:  
       split_formula.append(formula[start:len(formula)])  
  
    return split_formula

def split_at_digit(formula):
    digit_location = 1
    for char in formula[1:]:
        if char.isdigit():
            break
        digit_location += 1
    if digit_location == len(formula):
        return (formula, 1)
    return (formula[:digit_location], int(formula[digit_location:]))

def count_atoms_in_molecule(molecular_formula):
    atom_counts = {}
    start = 0
    
    for end in range(1, len(molecular_formula)):
        if molecular_formula[end].isupper():
            formula_part = molecular_formula[start:end]
            atom_name, atom_count_str = split_at_digit(formula_part)
            atom_count_int = int(atom_count_str)

            if atom_name not in atom_counts:
                atom_counts[atom_name] = atom_count_int
            else:
                atom_counts[atom_name] += atom_count_int

            start = end

    if start < len(molecular_formula):
        formula_part = molecular_formula[start:]
        atom_name, atom_count_str = split_at_digit(formula_part)
        atom_count_int = int(atom_count_str)
        
        if atom_name not in atom_counts:
            atom_counts[atom_name] = atom_count_int
        else:
            atom_counts[atom_name] += atom_count_int

    return atom_counts

    # Step 1: Initialize an empty dictionary to store atom counts
        
        # Step 2: Update the dictionary with the atom name and count

    # Step 3: Return the completed dictionary



def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
