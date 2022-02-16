wall_lecth=float(input('Please enter the length of the wall in m: '))
brick_lencth=float(input('Please enter the length of a brick in cm: '))
nbrick=round((wall_lecth*100)/brick_lecth)

left_over_lecth=Area_painted%single_pot
print(f'{nbrick} bricks build one row of wall.')
print(f'This is {(wall_lecth*100)%brick_lecth} cm short of the required wall length.')