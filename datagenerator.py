from neo4j import GraphDatabase
import random
import json
import pandas as pd
from date_generation import date_generation

# random.seed(0)

r = random.Random(0)

uri = "neo4j://localhost:7687"
driver = GraphDatabase.driver(uri, auth=(
    "neo4j", "test123"))
session = driver.session()
result = session.run(
    "MATCH (product:Product)-[relation:relatedTo]-(product2:Product) RETURN product.id, relation.correlation, product2.id")

product_matrix = []

previous_id = 0
for record in result:
    print(record)

    if(record['product.id'] != previous_id):
        product_matrix.append([record['product.id'], [], []])
        previous_id = record['product.id']

    product_matrix[-1][1].append(int(record['relation.correlation']))
    product_matrix[-1][2].append(record['product2.id'])

payslips = []

for i in range(10000):
    payslips.append([])

# add first product
for payslip in payslips:
    payslip.append(r.randrange(1, 10))

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

# add further products
for payslip in payslips:
    # select a r length the payslip should have (between 1 and 10)
    payslip_length = r.randrange(1, 11)
    while payslip_length > 1:

        # get last product on payslip for getting neo4j distances (or should this only be based on first added product?)
        last_product = payslip[-1]
        for i in product_matrix:
            if (i[0] == last_product):
                payslip.append(r.choices(i[2], i[1], k=1)[0])

        payslip_length -= 1

session.close()
driver.close()

# save payslip data to csv
payslip_df = pd.DataFrame(payslips)
payslip_df.to_csv('payslips.csv', index=False)


# create further payslip data (date, product amount etc.)
# payslip_db = []
# for payslip in payslips:
#     # for the payslip database add to each row payslip id, customer id and date
#     date = date_generation.get_generated_date()
#     print(date[1])
#     payslip_db.append([payslips.index(payslip), r.randint(
#         0, 99), date[0]])
#     print(payslip_db[-1])
