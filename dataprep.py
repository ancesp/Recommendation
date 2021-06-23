import csv
import pyodbc
import pandas as pd

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SWDMNZHLQ5\SQLEXPRESS;'
                      'Database=datagen;'
                      'Trusted_Connection=yes;')

# select ps.payslip_id, c.customer_id, c.customer_name, ps.payslip_date, p.product_id, p.product_name, p.product_category, ppt.amount, p.product_price from payslips ps left join customers as c on ps.customer_id=c.customer_id left join p_products_test as ppt on ps.payslip_id=ppt.payslip_id left join products as p on p.product_id=ppt.product_id order by c.customer_id, ps.payslip_id
df = pd.read_sql_query('select * from products', conn)
df.to_csv('products.csv', index=False)
