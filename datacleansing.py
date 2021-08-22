import pandas as pd
import csv

payslips_df = pd.read_csv('./test_payslips.csv')

double_product = 0

df_shape = payslips_df.shape
n_of_transactions = df_shape[0]
n_of_products = df_shape[1]

records = []
for i in range(0, n_of_transactions):
    # print(i)
    records.append([])
    for j in range(0, n_of_products):
        if ((str(payslips_df.values[i, j]) != 'nan')):
            # print("--")
            records[i].append(str(payslips_df.values[i, j]))

# Step 1: check for multiple seasonal products and remove
contains_seasonal_product = False
seasonal_product = 0
for payslip in records:

    # print("before", payslip)

    for product in payslip:

        # print(product)
        if (contains_seasonal_product == False and (product == '5' or product == '7')):
            # print("in if")
            contains_seasonal_product = True
            seasonal_product = product

        if (contains_seasonal_product == True and (product == '5' or product == '7')):
            if (seasonal_product != product):
                payslip.remove(product)

    contains_seasonal_product = False
    seasonal_product = 0

# Step 2: Check for double products and remove
for payslip in records:

    for product in payslip:

        #print(payslip[0], payslip.index(product), payslip.__len__())
        if(payslip.index(product) != payslip.__len__() - 1):
            print(payslip[payslip.index(product) + 1])
            for double_product in payslip[payslip.index(product) + 1:]:

                if(product == double_product):
                    payslip.remove(double_product)


records_df = pd.DataFrame(records)
records_df.to_csv('payslips_w_irr.csv', index=False)
