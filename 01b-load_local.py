import pandas as pd

base = pd.read_csv('base.csv')
base = base.drop('Unnamed: 0', axis = 1)
base.head().T.to_csv('data_example.csv') # outputting another data example, columns + 5 sample records
print 'DataFrame loaded into base, {} records'.format(len(base))

try:
    lookup = pd.read_csv('lookup.csv', index_col = 'Unnamed: 0')
    print 'DataFrame loaded into lookup, {} records'.format(len(lookup))
except:
    print 'You have no access to the lookup file, which is used for troubleshooting during the exploratory phase only.'