#!/bin/bash

## Slurm job parameters ##

#SBATCH --job-name=____queue
#SBATCH -N 1
#SBATCH -n 32
#SBATCH --time=144:00:00
#SBATCH -p rack1,rack2,rack3
#SBATCH --hint=nomultithread
#SBATCH --exclusive

## Number of simulations ##
sims=1

## Don't change below

cd $SLURM_SUBMIT_DIR

cd Main_Code

conda activate POS

for i in $(seq 1 $sims)

do 

echo "Before POS_gen"

python POS_gen.py 

module load vasp

echo "SLURM_JOBID="$SLURM_JOBID

echo "Working directory =" $SLURM_SUBMIT_DIR

mpirun -np $SLURM_NTASKS /bin/bash -c "ulimit -s unlimited; vasp_std"

mv POSCAR POSCAR_og_$i
mv KPOINTS KPOINTS_og
mv INCAR INCAR_og

mv CONTCAR POSCAR
mv KPOINTS_fine KPOINTS
mv INCAR_fine INCAR

./VASP_del.sh

check=0
while [ $check==0 ]
do

echo "in while"

mpirun -np $SLURM_NTASKS /bin/bash -c "ulimit -s unlimited; vasp_std"

if ! grep -q " 4 F= " OSZICAR 

  then

    break

fi

mv CONTCAR POSCAR

./VASP_del.sh

done

mv KPOINTS KPOINTS_fine
mv INCAR INCAR_fine
#
mv KPOINTS_og KPOINTS
mv INCAR_og INCAR

mv OUTCAR OUTCAR_$i
mv CONTCAR CONTCAR_$i

./VASP_del.sh
done
echo "FINISHED"
