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
    # print(record)

    if(record['product.id'] != previous_id):
        product_matrix.append([record['product.id'], [], []])
        previous_id = record['product.id']

    product_matrix[-1][1].append(int(record['relation.correlation']))
    product_matrix[-1][2].append(record['product2.id'])
    # print(product_matrix[-1])
# product_distances =


payslips = []

for i in range(10000):
    payslips.append([])

# print(payslips.__len__())

# add first product
for payslip in payslips:
    payslip.append(r.randrange(1, 10))

# get probabilities for items
sum_distances = 0
for i in product_matrix:
    if (i[0] == 17):
        print(sum(i[1]))
        test = 0
        for item in i[2]:
            print("the probability of item ", item,
                  "is", i[1][test] / sum(i[1]))
            test += 1
        #print(r.choices(i[2], i[1], k=1)[0])
        #payslip.append(r.choices(i[2], i[1], k=1)[0])

for payslip in payslips:
    # select a r length the payslip should have (between 1 and 10 + 1)
    payslip_length = r.randrange(1, 11)
    while payslip_length > 1:

        # get last product on payslip for getting neo4j distances
        last_product = payslip[-1]
        for i in product_matrix:
            if (i[0] == last_product):
                #print(r.choices(i[2], i[1], k=1)[0])
                payslip.append(r.choices(i[2], i[1], k=1)[0])

        # add more products
        #payslip.append(r.randrange(1, 37))
        payslip_length -= 1
    # print(payslip)

session.close()
driver.close()

print(date_generation.get_generated_date())

payslip_db = []

for payslip in payslips:
    # for the payslip database add to each row payslip id, customer id and date
    date = date_generation.get_generated_date()
    print(date[1])
    payslip_db.append([payslips.index(payslip), r.randint(
        0, 99), date[0]])
    print(payslip_db[-1])

payslip_df = pd.DataFrame(payslips)
payslip_df.to_csv('payslips.csv', index=False)
