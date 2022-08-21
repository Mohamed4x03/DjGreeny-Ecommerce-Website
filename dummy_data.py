from calendar import c
import os
from unicodedata import category
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project.settings')

import django
django.setup()

from faker import Faker
import random
from products.models import Product , Brand , Category


def seed_brand(n): #20
    fake = Faker()
    images=['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg','11.jpg','12.jpg','13.jpg','14.jpg','15.jpg','16.jpg','17.jpg','18.jpg','19.jpg']

    for _ in range(n):
        name = fake.name()
        image = f"brand/{images[random.randint(0,18)]}"
        Brand.objects.create(
            name=name,
            image=image
        )
    print(f"seed {n} Brand")    
        


def seed_category(n): #20
    fake= Faker()
    images=['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg','11.jpg','12.jpg','13.jpg','14.jpg','15.jpg','16.jpg','17.jpg','18.jpg','19.jpg']

    for _ in range(n):
        name = fake.name()
        image = f"Category/{images[random.randint(0,18)]}"
        Category.objects.create(
            name=name,
            image=image
        )
    print(f"seed {n} Category")    
        

def seed_products(n):
    fake = Faker()

    flag_type=['new','feature']
    images=['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg','11.jpg','12.jpg','13.jpg','14.jpg','15.jpg','16.jpg','17.jpg','18.jpg','19.jpg','20.jpg']
    
    for _ in range(n):
        name = fake.name()
        sku = random.randint(1,10000)
        brand = Brand.objects.get(id=random.randint(1,20))
        price = round(random.uniform(20.99,99.99),2)
        desc = fake.text(max_nb_chars=1000)
        flag = flag_type[random.randint(0,1)]
        category = Category.objects.get(id=random.randint(1,20))
        image = f"Products/{images[random.randint(0,19)]}"
        
        Product.objects.create(
            
            name=name,
            sku=sku,
            brand=brand,
            price=price,
            desc=desc,
            flag=flag,
            category=category,
            image=image,
        )
    print(f"seed {n} Products")    



# seed_brand(20)
# seed_category(20)
# seed_products(10)