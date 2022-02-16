Area_painted=float(input('Enter the area in m2 to be painted: '))
single_pot=float(input('Enter the area (m2) that a single pot covers: '))

npots=round(Area_painted/single_pot)
left_over=Area_painted%single_pot

print(f'You will need {npots} pots of paint.')
print(f'You can paint {left_over} m2 with the leftover paint.')
