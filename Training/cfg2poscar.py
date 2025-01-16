import re
import glob

def process_cfg_file(filename, file_index):
    with open(filename, 'r') as file:
        content = file.read()

    sections = re.findall(r"BEGIN_CFG(.*?)END_CFG", content, re.DOTALL)

    structures = []
    
    for section_index, section in enumerate(sections):
        # Extract the number of atoms
        size_match = re.search(r"Size\s+(\d+)", section)
        num_atoms = int(size_match.group(1)) if size_match else 0

        # Extract the supercell matrix (3x3)
        supercell_match = re.search(r"Supercell(.*?)AtomData", section, re.DOTALL)
        supercell_lines = supercell_match.group(1).strip().splitlines()
        supercell = [list(map(float, line.split())) for line in supercell_lines]

        # Extract AtomData and forces, and count atom types
        atomdata_match = re.search(r"AtomData:(.*?)Energy", section, re.DOTALL)
        atomdata_lines = atomdata_match.group(1).strip().splitlines()[1:num_atoms+1]
        data = []
        atom_types = {}
        for line in atomdata_lines:
            parts = line.split()
            atom_type = int(parts[1])  # The second column is the atom type
            forces = list(map(float, parts[2:]))  # Extract the last 6 columns
            data.append(forces)
            atom_types[atom_type] = atom_types.get(atom_type, 0) + 1

        # Extract energy
        energy_match = re.search(r"Energy\s+([\-\d\.]+)", section)
        energy = float(energy_match.group(1)) if energy_match else 0.0

        # Extract stress (skip the header line starting with 'xx', and capture the 6 numeric values)
        stress_match = re.search(r"PlusStress:.*?\n\s*([\d\.\-\s]+)", section)
        if stress_match:
            stress_line = stress_match.group(1).strip()
            stress = list(map(float, stress_line.split()))

        else:
            stress = [0.0] * 6

        # Prepare the structure output
        structure_output = []
        structure_output.append(f"structure {file_index}, the last 3 columns after Cartesian are fx,fy,fz || Total Energy: [{energy}] || Stress : {stress}")
        structure_output.append("1.0")  # Line with fixed value
        structure_output.extend([" ".join(map(str, row)) for row in supercell])  # Add supercell

        # Prepare the types for line 6 and counts for line 7
        types = sorted(atom_types.keys())  # Sorted list of distinct atom types
        structure_output.append(" ".join([f"type_{t}" for t in types]))  # e.g., type_0, type_1, etc.
        atom_counts = " ".join(str(atom_types[t]) for t in types)  # Number of atoms for each type
        structure_output.append(atom_counts)

        structure_output.append("Cartesian")  # Cartesian line
        
        # Add the atomic data (forces)
        structure_output.extend([" ".join(map(str, forces)) for forces in data])
        
        structures.append("\n".join(structure_output))
    
    return structures

def process_all_cfg_files():
    cfg_files = glob.glob("*.cfg")
    
    all_structures = []
    for idx, cfg_file in enumerate(cfg_files, 1):
        structures = process_cfg_file(cfg_file, idx)
        all_structures.extend(structures)
    
    # Write the structures to output files
    for i, structure in enumerate(all_structures, 1):
        with open(f"structures_{i}.POSCAR", "w") as f:
            f.write(structure)

if __name__ == "__main__":
    process_all_cfg_files()

