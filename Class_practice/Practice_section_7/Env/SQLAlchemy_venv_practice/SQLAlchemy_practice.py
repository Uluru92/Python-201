import sqlalchemy
from Examples.actor import Actor
  
engine = sqlalchemy.create_engine('mysql+pymysql://root:Coloresl2l2!@localhost/sakila')  
connection = engine.connect()
metadata = sqlalchemy.MetaData()  

actor = sqlalchemy.Table('actor', metadata, autoload_with=engine)
  
query = sqlalchemy.select(actor)
result_proxy = connection.execute(query)

actor_list = []
  
for result in result_proxy:
    new_actor = Actor(result[0], result[1], result[2], result[3])
    actor_list.append(new_actor)

for actor in actor_list:
    print(actor)