Molecule Relaxation for Amorphous Structures (MRAS) code is made for SLURM script with computing clusters on Linux systems. The density functional theory is done through VASP and a license is required to run the code. 
Necessary packages needed: 
VASP - https://www.vasp.at/
Numpy - https://anaconda.org/anaconda/numpy

Directions to use the Amorphous structure construction workflow:

Necessary POTCAR for the system analysis is needed for the analysis. Produce the appropriate POTCAR and add it to the Main_Code file.

Open POS_gen.py and adjust mols, posit, num_mol, cell, and dist

-mols is the array displaying the different molecules  [["molecule1_atom1_type","molecule1_atom2_type",...],["molecule2_atom1_type,"molecule2_atom2_tye",...],...] 

-posit is the array displaying the positions of the atoms in the molecules [[[molecule1_atom1_pos],[molecule1_atom2_pos],...],[[molecule2_atom1_pos],[molecule2_atom2_pos],...],...]

-num_mol is the number of molecules in the cell [mol1_num,mol2_num,...]

-cell is the cubic cell parameters [x,y,z]. To get the lengths: length = ((total molecular weight) * 9 / .6022 / den_crystal)^(1/3) 

- dist is minimum seperation distance. Obtained through the minimum energy configuration of the longest molecule multiplied by 1.5 for stochiometry <=3 or 1.5 of the longest molecule for a segmented molecule of stochiometry > 3.


In Submission_Script.sh, number of simulations to run is controlled by 'sims' variable. 
