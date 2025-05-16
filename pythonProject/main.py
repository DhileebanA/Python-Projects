from prettytable import *

x = PrettyTable()
x.add_column('Pokemon', ['Pickachu', 'Salsar', 'Waty'])
x.align = 'l'
x.add_column('Type', ['Electric', 'Fire', 'Water'])
print(x)