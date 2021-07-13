import pandas as pd
import csv

database_df = pd.read_csv('./database_data_old.csv')

database = []

customer_id = 0
payslip_id = 0


for row in database_df.iterrows():
    customer = [row[1]['customer_id'], row[1]['customer_name'], []]

    if(customer_id != row[1]['customer_id']):
        database.append(customer)
        customer_id = row[1]['customer_id']

    payslip = [row[1]['payslip_id'], row[1]['payslip_date'], []]
    customer_payslips = database[database.__len__() - 1][2]

    if(payslip_id != row[1]['payslip_id']):
        customer_payslips.append(payslip)
        payslip_id = row[1]['payslip_id']

    product = [row[1]['product_id'], row[1]['product_name'], row[1]
               ['product_category'], row[1]['amount'], row[1]['product_price']]
    payslip_products = customer_payslips[customer_payslips.__len__() - 1][2]
    payslip_products.append(product)


# Data Cleansing

# Step 1: Check for Products with amount 0

products_with_0_amount = []
for customer in database:

    for payslip in customer[2]:

        for product in payslip[2]:
            if(product[3] == 0):
                products_with_0_amount.append(product)

        for product in products_with_0_amount:
            payslip[2].remove(product)

        products_with_0_amount = []


# Step 2: Check for double products

for customer in database:

    for payslip in customer[2]:

        for product in payslip[2]:

            for double_product in payslip[2][payslip[2].index(product) + 1:]:

                if(product[1] == double_product[1]):
                    payslip[2].remove(double_product)


# Step 3: Check for double datetimes

for customer in database:
    print("before", customer[2].__len__())
    for payslip in customer[2]:

        for double_date_payslip in customer[2][customer[2].index(payslip) + 1:]:

            if(payslip[1] == double_date_payslip[1]):
                customer[2].remove(double_product)
    print("after", customer[2].__len__())


# print table
price = 0

for customer in database:
    print("-----------------------")
    print(customer[1])

    for payslip in customer[2]:
        print("       ", payslip[0], "-", payslip[2].__len__(), "products")

        for product in payslip[2]:
            print("           ", product[1], product[3])
            price = price + product[4]
        print("                  ", "~", "Total price:", price)
        price = 0


product_data = []

for customer in database:

    for payslip in customer[2]:
        new_product_list = []

        for product in payslip[2]:
            new_product_list.append(product[0])

        product_data.append(new_product_list)


product_data_df = pd.DataFrame(product_data)
product_data_df.to_csv('product_data_ids.csv', index=False)
