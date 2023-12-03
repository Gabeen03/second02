import pandas as pd
from faker import Faker as fk
import os

# temp = fk()
temp = fk("ko-KR")
print(temp.name())

folder = "data/"
if not os.path.isdir(folder) :
    os.mkdir(folder)
with open(folder + "fktemp.csv", "w", encodung='utf8') as f : 
    f.write("name, adress, postcode, company, job, phone, email, id, ip_pub, catch_")

with open(folder + "fktemp.csv", "a", encodung='utf8') as f : 
    for i in range(30) :
        f.write(temp.name() + "," +
                temp.adredd() + ","+
                )


target = folder + "fktemp.sv"

