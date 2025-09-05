from my_postgresql import MyDenodoDB

my_denodo_object = MyDenodoDB()
my_denodo_object.connect()
print(my_denodo_object.query_to_df("SELECT 1 as COLNAME"))
my_denodo_object.close()

