print('Please enter the volume of the jar (cm3): ')
jar_volume=float(input(''))
print('Please enter the volume of one sweet (cm3): ')
sweet_volume=float(input(''))
N_sweets=str(round(jar_volume/sweet_volume, 1))[:4]
print()
print(f'{N_sweets} sweets fit into the jar.')