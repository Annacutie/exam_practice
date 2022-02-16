sentence=input("Enter sentence of your choise:")

a=list(sentence).count('a')
e=list(sentence).count('e')
i=list(sentence).count('i')
o=list(sentence).count('o')
u=list(sentence).count('u')

print(f"a={a}")
print(f"e={e}")
print(f"i={i}")
print(f"o={o}")
print(f"u={u}")

print(f'this is a total of {a+e+i+o+u} voweles.')