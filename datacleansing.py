import pandas as pd
import csv

payslips_df = pd.read_csv('./payslips.csv')

double_product = 0

df_shape = payslips_df.shape
n_of_transactions = df_shape[0]
n_of_products = df_shape[1]

records = []
for i in range(0, n_of_transactions):
    records.append([])
    for j in range(0, n_of_products):
        if (str(payslips_df.values[i, j]) != 'nan'):
            records[i].append(str(int(payslips_df.values[i, j])))

# print(records)

contains_seasonal_product = False
seasonal_product = 0
for payslip in records:

    #print("before", payslip)

    for product in payslip:

        # print(product)
        if (contains_seasonal_product == False and (product == '5' or product == '7')):
            print("in if")
            contains_seasonal_product = True
            seasonal_product = product

        if (contains_seasonal_product == True and (product == '5' or product == '7')):
            if (seasonal_product != product):
                payslip.remove(product)

    contains_seasonal_product = False
    seasonal_product = 0


#         for double_product in payslip.index(product):

#             if(product[1] == double_product[1]):
#                 payslip[2].remove(double_product)
    print("after", payslip)

records_df = pd.DataFrame(records)
records_df.to_csv('payslips_cleaned.csv', index=False)
