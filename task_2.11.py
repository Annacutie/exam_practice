product_name=input('Please enter product name: ').split(" ")
year=input('Please enter the year: ')
print(f'{product_name[0][:2]}{product_name[1][3:]}{year[:1]}{year[3:]}')