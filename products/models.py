from database import db
import peewee


class Product(peewee.Model):
    title = peewee.CharField(max_length=30)
    body = peewee.TextField()
    image = peewee.CharField(max_length=150, unique=True)
    price = peewee.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        database = db


class Gallery(peewee.Model):
    product = peewee.ForeignKeyField(Product, on_delete='CASCADE', backref='galleries')
    image = peewee.CharField(max_length=150, unique=True)

    class Meta:
        database = db
