import pandas as pd

base = pd.read_csv('base.csv')
base = base.drop('Unnamed: 0', axis = 1)
base.head().T.to_csv('data_example.csv') # outputting another data example, columns + 5 sample records
print 'DataFrame loaded into base, {} records'.format(len(base))

lu_ptype = {
            1001 : 'SFR',
            1002 : 'TOWNHOUSE',
            1003 : 'CLUSTER HOME',
            1004 : 'CONDO',
            1005 : 'COOP',
            1006 : 'MOBILE',
            1007 : 'ROW HOUSE',
            1009 : 'SFR-PUD',
            1101 : 'MFR',
            1102 : 'MFR',
            1103 : 'MFR',
            1110 : 'MFR'
            }

base['ptype'] = base.LAND_USE.map(lu_ptype)

basef = base

basef = basef[basef.ASSESSED_TOTAL_VALUE > 0] # remove Land
basef = basef[basef.FIDELITY_LATITUDE > 0] # remove properties with no lat/long information
basef = basef[basef.ASSESSED_LAND_VALUE > 0] # remove properties with no land value
basef = basef[basef.BUILDING_AREA > 0] # remove properties with no land value
basef = basef[basef.BED > 0]
basef = basef[basef.BATH > 0]
basef = basef[basef.STORIES > 0]

basef2 = basef

basef2 = basef2[basef2.AGE.notnull()]
basef2 = basef2[basef2.ptype.notnull()]
basef2 = basef2[basef2.STORIES.notnull()]

basef2 = basef2[basef2.STORIES != 'S/L']
basef2.STORIES = basef2.STORIES.replace(r'\+B*', '', regex = True)
basef2.STORIES = basef2.STORIES.astype(float)

# looks like lot size has mixed units (feet, acres): I'll attempt to convert acres to feet using the following rule:
basef2['lsize_sqft'] = basef2.LOT_SIZE.apply(lambda x: x * 43560 if x < 100 and x < basef2.BUILDING_AREA.iteritems() else x)

basef2['landval_perc'] = basef2.ASSESSED_LAND_VALUE / basef2.ASSESSED_IMP_VALUE
basef2['lot_perc'] = 1 - basef2.BUILDING_AREA / basef2.lsize_sqft

basef2 = basef2[basef2.lot_perc >= -0.1]
basef2 = basef2[basef2.PARKING <= 10]
basef2 = basef2[basef2.TOTAL_UNITS < 3.5]
basef2 = basef2[basef2.STORIES < 4.5]
print 'Processed, {} records remaining'.format(len(basef2))