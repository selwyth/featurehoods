# pulling from Oracle transaction database at work
import cx_Oracle
import pandas as pd
import yaml
import os 

cred = yaml.load(open(os.path.expanduser('prod_cred.yml')))
conn = cx_Oracle.connect(cred['USER'] + '/' + cred['PW'] + '@PROD')
base = pd.io.sql.read_sql(
    """
    select full_address, assessed_land_value, assessed_total_value, assessed_imp_value, 
        zip, 
        full_bathroom_count + partial_bathroom_count * 0.5 bath,
        bedroom_count as bed,
        2009 - year_built as age,
        stories,
        garage_type,
        parking,
        total_units,
        land_use,
        pool,
        fireplace,
        property_type,
        building_area,
        lot_size,
        fidelity_latitude,
        fidelity_longitude
        
        from bdr.fidelity_assessment_record f
        JOIN bdr.zipcode_city_mapping zcm ON f.zip = zcm.zipcode
        WHERE zcm.mls_table = 'MLS_CA_BA'
        and assessment_year = 2009
        and lot_size > 0
    ORDER BY address_id
    """, conn)

lookup = base.FULL_ADDRESS
base = base.drop('FULL_ADDRESS', axis = 1)

base.to_csv(path_or_buf = 'base.csv') # this outputs the csv file for analysis
lookup.to_csv('lookup.csv') # this outputs the lookup for the anonymized properties

from sklearn.cross_validation import train_test_split

base_l, base_s = train_test_split(base, test_size = 1000, random_state = 32)
base_s = pd.DataFrame(base_s, columns = base.columns)
base_s.to_csv('base_s.csv') # this outputs a sample 1000 rows

print 'SQL executed, file saved locally as base.csv'