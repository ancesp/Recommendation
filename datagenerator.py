from neo4j import GraphDatabase
import random
import json
import pandas as pd
from date_generation import date_generation

# random.seed(0)
r = random.Random(0)

# connect to Neo4j Database
uri = "neo4j://localhost:7687"
driver = GraphDatabase.driver(uri, auth=(
    "neo4j", "test123"))
session = driver.session()
result = session.run(
    "MATCH (product:Product)-[relation:relatedTo]-(product2:Product) RETURN product.id, relation.correlation, product2.id")

# create product matrix and save products with their correalation to other products
product_matrix = []

previous_id = 0
for record in result:

    if(record['product.id'] != previous_id):
        product_matrix.append([record['product.id'], [], []])
        previous_id = record['product.id']

    product_matrix[-1][1].append(int(record['relation.correlation']))
    product_matrix[-1][2].append(record['product2.id'])

# create payslips
payslips = []

for i in range(715):
    payslips.append([])

# add first product
for payslip in payslips:
    payslip.append(r.randrange(1, 10))

payslip_lengths = []

# define length of each payslip so that the mean of all payslips is ~6
# ????????
# for i in range(715):

# get probabilities for items
sum_distances = 0
for i in product_matrix:
    if (i[0] == 1):
        print(sum(i[1]))
        test = 0
        for item in i[2]:
            print("the probability of item ", item,
                  "is", i[1][test] / sum(i[1]))
            test += 1

irrelevant_product_index = 0
irrelevant_product = "product"

# add further products
for payslip in payslips:

    # select a random length the payslip should have (between 1 and 15)
    payslip_length = r.randrange(1, 16)

    # select how many irrelevant products should be in the payslip
    number_irrelevant_products = r.randrange(1, payslip_length + 1)

    while payslip_length > 1:

        if(payslip_length > number_irrelevant_products + 1):

            # get last product on payslip for getting neo4j distances (or should this only be based on first added product?)
            last_product = payslip[-1]
            for i in product_matrix:
                if (i[0] == last_product):
                    payslip.append(r.choices(i[2], i[1], k=1)[0])
        else:
            payslip.append(irrelevant_product + str(irrelevant_product_index))
            irrelevant_product_index += 1

        payslip_length -= 1

session.close()
driver.close()

# save payslip data to csv
payslip_df = pd.DataFrame(payslips)
payslip_df.to_csv('test_payslips.csv', index=False)
