cir=int(input('What is the circumference of your wheel in millimetres? '))

d=cir/1000000*wr
wr=int(input('How many wheel revolutions have taken place in your journey? '))

t=int(float('How many minutes did you cycle for? '))

s=d/t

print(f'You covered {d} km.')
print(f'At an average speed of {s} kmh.')