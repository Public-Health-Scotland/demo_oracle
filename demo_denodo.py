# import class from python script
from my_postgresql import MyDenodoDB

# create an object
my_denodo_object = MyDenodoDB()
# open a connection
my_denodo_object.connect()
# print a retrieved datafraame
print(my_denodo_object.query_to_df("SELECT 1 as COLNAME, CURRENT_TIMESTAMP as datetime"))
# close connection
my_denodo_object.close()
