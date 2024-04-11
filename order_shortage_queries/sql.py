import sqlite3
import pandas as pd

conn = sqlite3.connect('orders.db')
cur = conn.cursor()

# reading the tables

order_df = pd.read_excel(r"/home/bachan/Downloads/order file.xlsx")
corr_df = pd.read_excel(r"/home/bachan/Downloads/items-correlation.xlsx")
rca_df = pd.read_csv(r"/home/bachan/Downloads/RCA.csv")

def column_formatting(df):
    for col in df.columns:
        formatted_col = col.lower().strip().replace(' ','_')
        df.rename(columns={col:formatted_col},inplace=True)
    return df
    
order_df = column_formatting(order_df)
corr_df = column_formatting(corr_df)
rca_df = column_formatting(rca_df)

def to_database(df,table_name,conn):
    df.to_sql(table_name,conn,if_exists='append',index=False)

to_database(order_df,'orders',conn)
to_database(corr_df,'correlation_master',conn)
to_database(rca_df,'rca',conn)

conn.commit()
conn.close()

print('Data Inserted Successfully..')
