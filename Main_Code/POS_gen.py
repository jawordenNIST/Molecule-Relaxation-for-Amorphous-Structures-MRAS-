# Import Package
import numpy as np
import random as rand
import time

# populate molecules and cartesian coordinates
mols = [["Si","Si"]]
posit = [[[0,0,0],[2.228335,0,0]]]

# Number of molecules per cell in array format
num_mol=[5]

# Cell parameters and minimum molecule distance
cell = [12.18,12.18,12.18]
dist = 3.3425025

#DONT CHANGE ANYTHING BELOW

# Uniform rotation in 3D space.
import numpy as np

def uniform_random_rotation(x):
    """Apply a random rotation in 3D, with a distribution uniform over the
    sphere.

    Arguments:
        x: vector or set of vectors with dimension (n, 3), where n is the
            number of vectors

    Returns:
        Array of shape (n, 3) containing the randomly rotated vectors of x,
        about the mean coordinate of x.

    Algorithm taken from "Fast Random Rotation Matrices" (James Avro, 1992):
    https://doi.org/10.1016/B978-0-08-050755-2.50034-8
    """

    def generate_random_z_axis_rotation():
        """Generate random rotation matrix about the z axis."""
        R = np.eye(3)
        x1 = np.random.rand()
        R[0, 0] = R[1, 1] = np.cos(2 * np.pi * x1)
        R[0, 1] = -np.sin(2 * np.pi * x1)
        R[1, 0] = np.sin(2 * np.pi * x1)
        return R

    # There are two random variables in [0, 1) here (naming is same as paper)
    x2 = 2 * np.pi * np.random.rand()
    x3 = np.random.rand()

    # Rotation of all points around x axis using matrix
    R = generate_random_z_axis_rotation()
    v = np.array([
        np.cos(x2) * np.sqrt(x3),
        np.sin(x2) * np.sqrt(x3),
        np.sqrt(1 - x3)
    ])
    H = np.eye(3) - (2 * np.outer(v, v))
    M = -(H @ R)
    x = x.reshape((-1, 3))
    mean_coord = np.mean(x, axis=0)
    return ((x - mean_coord) @ M) + mean_coord @ M

# rotation function.
def rot(p):
    cont=0
    temp_at=[]
    temp_pos=[]
    ti=time.time()
    while cont==0:
        temp_at=[]
        temp_pos=[]
        rot=uniform_random_rotation(np.array([[1,0,0],[0,1,0],[0,0,1]]))
        breaker=0

        # Position atom
        xph=rand.random()*cell[0]
        yph=rand.random()*cell[1]
        zph=rand.random()*cell[2]
        for i in range(0,len(mols[p])):
            # Rotate atom
            xtemp=posit[p][i][0]*rot[0][0]+posit[p][i][1]*rot[0][1]+posit[p][i][2]*rot[0][2]
            ytemp=posit[p][i][0]*rot[1][0]+posit[p][i][1]*rot[1][1]+posit[p][i][2]*rot[1][2]
            ztemp=posit[p][i][0]*rot[2][0]+posit[p][i][1]*rot[2][1]+posit[p][i][2]*rot[2][2]
            xtemp=xtemp+xph
            if xtemp > cell[0]:
                 xtemp=xtemp-cell[0]
            elif xtemp < 0:
                 xtemp=xtemp+cell[0]
            ytemp=ytemp+yph
            if ytemp > cell[1]:
                 ytemp=ytemp-cell[1]
            elif ytemp < 0:
                 ytemp=ytemp+cell[1]
            ztemp=ztemp+zph
            if ztemp > cell[2]:
                 ztemp=ztemp-cell[2]
            elif ztemp < 0:
                 ztemp=ztemp+cell[2]
            #Check nearest neighbor
            for k in range(0,len(cell_pos)):
                for j in range(0,len(cell_pos[k])):
                     xrad=abs(xtemp-cell_pos[k][j][0])
                     if xrad > (cell[0]/2):
                         xrad-=cell[0]
                     yrad=abs(ytemp-cell_pos[k][j][1])
                     if yrad > (cell[1]/2):
                         yrad-=cell[1]
                     zrad=abs(ztemp-cell_pos[k][j][2])
                     if zrad > (cell[2]/2):
                         zrad-=cell[2]
                     rad = (xrad**2 + yrad**2 + zrad**2)**(1/2)
                     if rad < dist:
                         breaker=1
                         break
                if breaker==1:
                    break
            if breaker==1:
                 break
            temp_at.append(mols[p][i])
            temp_pos.append([xtemp,ytemp,ztemp])
        if breaker==0:
            atom_typ.append(temp_at)
            cell_pos.append(temp_pos)
            cont=1
            return 0
        te=time.time()
        elapse=(te-ti)
        if elapse>30:
            cont=1
            return 1



# Iterating through all the molecules
cell_pos=[]
atom_typ=[]
num=1
while num == 1:
    cell_pos=[]
    atom_typ=[]
    for i in range(0,len(mols)):
        for k in range(0,num_mol[i]):
            num = rot(i)
#            print(num,cell)
            if num == 0:
                pass
            if num == 1:
                cell[0]=cell[0]+.1
                cell[1]=cell[1]+.1
                cell[2]=cell[2]+.1
                break
        if num == 1:
            break

# Make Poscar File for system
types_arr=[]
nums_arr=[]
pos_fin=[]
for i in range(0,len(atom_typ)):
    for j in range(0,len(atom_typ[i])):
        for k in range(0,len(types_arr)):
            if atom_typ[i][j]==types_arr[k]:
                nums_arr[k]=nums_arr[k]+1
                break
            if k==len(types_arr)-1:
                types_arr.append(atom_typ[i][j])
                nums_arr.append(1)
        if len(types_arr)==0:
            types_arr.append(atom_typ[i][j])
            nums_arr.append(1)

for i in range(0,len(types_arr)):
    for j in range(0,len(atom_typ)):
        for k in range(0,len(atom_typ[j])):
            if types_arr[i] == atom_typ[j][k]:
                pos_fin.append(cell_pos[j][k])

# Begin writing POSCAR file. 

#print("Before POSCAR")

POSCAR = open(r"POSCAR","w")

POSCAR.write("System " + str(len(atom_typ))+'\n')
POSCAR.write("1.0"+'\n')
POSCAR.write(str(cell[0]) +" 0 0"+'\n')
POSCAR.write("0 "+ str(cell[1])+ " 0"+'\n')
POSCAR.write("0 0 "+str(cell[2])+'\n')
line_at=''
line_num=''
for i in range(0,len(types_arr)):
    line_at=line_at+types_arr[i]+'  '
    line_num=line_num+str(nums_arr[i])+'  '
line_at=line_at+'\n'
line_num=line_num+'\n'
POSCAR.write(line_at)
POSCAR.write(line_num)

POSCAR.write("Cartesian \n")
for i in range(0,len(pos_fin)):
    line_cart=''
    for k in range(0,len(pos_fin[i])):
        line_cart=line_cart+str(pos_fin[i][k])+' '
    line_cart=line_cart+'\n'
    POSCAR.write(line_cart)


POSCAR.close()
