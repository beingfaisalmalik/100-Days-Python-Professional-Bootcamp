#module is single file
#pacakage is multiple file

from prettytable import PrettyTable
table = PrettyTable()
table.add_column('Pokemon Name',['Pikachu', 'Squirtle', 'Charmendar'])
table.add_column('Type',['Electric', 'Water', 'Fire'])
print(table)
table.align = 'l'
print(table)
