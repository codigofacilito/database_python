import peewee
import datetime

database = peewee.MySQLDatabase('dbpython', host='localhost', port=3306, user='root', passwd='')

class User(peewee.Model):
  username = peewee.CharField(unique=True, max_length=50, index=True)
  password = peewee.CharField(max_length=50, null=True)
  email = peewee.CharField(max_length=50)
  active = peewee.BooleanField(default=True)
  created_date = peewee.DateTimeField(default=datetime.datetime.now)

  class Meta:
    database = database
    db_table = 'users'

  def __str__(self):
    return self.username
    
class Store(peewee.Model):
  admin = peewee.ForeignKeyField(User, related_name='store') #primary_key=True Relacion uno a uno
  name = peewee.CharField(max_length=50, unique=50, index=True)
  address = peewee.TextField()
  active = peewee.BooleanField(default=True)
  created_date = peewee.DateTimeField(default=datetime.datetime.now)
  
  class Meta:
    database = database
    db_table = 'stores'

  def __str__(self):
    return self.name

class Product(peewee.Model):
  name = peewee.CharField(max_length=100)
  description = peewee.TextField()
  store = peewee.ForeignKeyField(Store, related_name='products') #ForeignKeyField allows for a backreferencing property to be bound to the target model. Implicitly, this property will be named classname_set, where classname is the lowercase name of the class, but can be overridden via the parameter related_name:
  price = peewee.DecimalField(max_digits=5, decimal_places=2) #100.00
  stock = peewee.IntegerField()
  created_date = peewee.DateTimeField(default=datetime.datetime.now)
  
  class Meta:
    database = database
    db_table = 'products'

  def __str__(self):
    return '{name} - ${price}'.format(name=self.name, price=self.price)

class Category(peewee.Model):
  name = peewee.CharField(max_length=100)
  description = peewee.TextField()
  created_date = peewee.DateTimeField(default=datetime.datetime.now)
  
  class Meta:
    database = database
    db_table = 'categories'

  def __str__(self):
    return '{name} - ${price}'.format(name=self.name, price=self.price)
