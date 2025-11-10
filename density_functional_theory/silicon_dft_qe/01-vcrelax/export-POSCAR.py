from ase.io import read, write

atoms = read('vcrelax.out', index=-1)
atoms.write('POSCAR')
