### Data for the Molecule Relaxation for Amorphous Structures (MRAS)

Workflow and final data for the Molecule Relaxation for Amorphous Structures (MRAS). The accompanying manuscript describing the methodology will be published.

## Initial Structural Investigations

Initial structural investigations through Silicon are documented in the directory Si_Base with varying initial volume and separation distances. Workflows are included in the directories with slurm Submission script: Submission_Script.sh

The CONTCAR file holds final system with density provided at top of file in grams / cm<sup>3</sup> with the average density of all the systems provided in Average_Den file. 

## Workflow

The individual materials investigation contain the directories of the files used for the workflow. This includes the POS_gen.py file that produces the initial structure that will be minimized through *ab initio* density functional theory (DFT) energy minimization calculations. This file is produced in a VASP POSCAR format. VASP software is used for the DFT calculations with the accompanying INCAR, KPOINTS, and POTCAR file used. The calculations are performed using SLURM scheduler and reflect the iterative relaxation process that should be followed in line with the methodology. 

# Instructions
The workflow can be visualized in the provided image.

a-b) Obtain energy minimized molecule of interest that will be used to populate initial structure. The methodology for obtaining the minimized molecule is not provided.

c) Use minimized molecule structure to fill out POS_gen.py file that will be used to produce the initial structure. The lines of code that need to be changed include:

1. mols 
  - Array containing the atomic structure of the molecules. E.g. mols = [[molecule1_atom1, molecule1_atom2, ...], [molecule2_atom1, molecule2_atom2, ...],...]

2. posit
  - Array containing the positions of atoms in cartesian coordinate system. E.g. posit = [[[molecule1_atom1_x, molecule1_atom1_y, molecule1_atom1_z],[molecule1_atom2_x, molecule1_atom2_y, molecule_1_atom2_z],...], [[molecule2_atom1_x, molecule2_atom1_y, molecule2_atom1_z], [molecule2_atom2_x, molecule2_atom2_y, molecule2_atom2_z], ...], ...]

3. num_mol
  - Array containing the number of molecules used in the system. E.g. num_mol = [number_of_molecule1, number_of_molecule2, ...]

4. cell
  - Array of the x, y, and z coordinates for the initial simulation box. E.g. cell = [x, y, z]

5. dist
  - Value of the minimum separation distance between molecules in Angstrom. 

d) Minimize structure through DFT. This involves an initial lower energy cutoff and kpoint mesh to increase the computational speed. After the first initial relaxation, a higher energy cutoff and kpoint mesh is used to obtain the final structure through iterative relaxations until the structure does not undergo additional structural change. 

<p align="center">
  <img width="433" alt="Si_rel" src="https://github.com/user-attachments/assets/7b6ef422-460e-4928-ae7b-6dadbaa09bf8" />
 
**Figure: Steps for creating amorphous structure. (a-b) DFT calculations for obtaining the energy minimized molecule. (c) Initial cell structure produced using the POS_gen.py file. (d) Iterative minimization method.** 
</p>

## Final data

Final data for the different amorphous structures (Si, SiO2, HfO2, ZrCu, and Al2O3) are provided in respective directories. 10 different systems displayed in CONTCAR files with the density provided in the header in grams / cm<sup>3</sup>. Workflow for each system is provided in Workflow directory with slurm Submission script: Submission_Script.sh.
