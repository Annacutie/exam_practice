3holes=int(input(int('How many par 3 holes are there? ')))

3par_shots=3*3holes

4holes=int(input(int(input('How many par 4 holes are there? ')))

4par_shots=4*4holes

5holes=int(input(int(input('How many par 4 holes are there? ')))

5par_shots=5*5holes

difficuty=int(input('What is the difficulty adjustment for the course? '))

print(f'The Standard Scratch score for the course is:{5par_shots + 4par_shots + 3par_shots + difficulty} shots in total')