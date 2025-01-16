## Potential Information
**Potential Name**: `Potential/AlTiV.mtp`  
-This potential was developed to accurately model the interactions in Al-Ti-V alloys for molecular dynamics simulations.
- Type 1: Al, Type 2: Ti, Type 3: V
---

## LAMMPS Simulation

### MLIP Package in LAMMPS
To use the MTP potential in LAMMPS, the **MLIP** package is required. You can find the MLIP package at the following repository:  
[MLIP-2 Interface for LAMMPS](https://gitlab.com/ashapeev/interface-lammps-mlip-2)

### Sample Calculations
A sample calculation for elastic constants can be found in the folder:  
`Ti_elasticConstant/`

This folder contains all necessary input files for LAMMPS simulations using the `AlTiV.mtp` potential to calcualte HCP Ti's elastic constant.

---

## DFT Database and Training

### Complete Training Database
The complete database used during the training of this potential is provided in the file:  
`altiv.cfg`

### Training Package
The potential was trained using the **MLIP-2** package.  
You can download the MLIP-2 package here:  
[MLIP-2 Download](https://mlip.skoltech.ru/download/)

---

## Helping Tools

### `cfg2poscar.py`
This Python script is included to facilitate the conversion of `.cfg` files to VASP POSCAR format.
- **Purpose**: Converts `.cfg` files into separate `structure_*.POSCAR` files, enabling visualization in OVITO.
- **Additional Information**: The generated `POSCAR` files retain energy, force, and stress information from the original `.cfg` files.

To use the script, copy the *.cfg file and code in same folder and run : ``` python cfg2poscar.py ``` 


## Contact Information

For questions or further assistance, please contact:  
**Mash**  
Email: [mash@lanl.gov](mailto:mash@lanl.gov)


