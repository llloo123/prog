# src/db/queries.py

from pypika import Query, Table, Field, functions as fn

products = Table('products')
users = Table('users')

# 2 запроса с JOIN
query1 = Query.from_(products).join(users).on(products.id == users.product_id).select(products.name, users.username)
query2 = Query.from_(users).join(products).on(users.product_id == products.id).select(users.username, products.price)

# 3 запроса с расчётом статистики/группировкой/агрегирующими функциями
query3 = Query.from_(products).select(fn.Avg(products.price))
query4 = Query.from_(products).groupby(products.category).select(products.category, fn.Sum(products.price))
query5 = Query.from_(users).groupby(users.username).select(users.username, fn.Count(users.product_id))

def get_queries():
    return query1.get_sql(), query2.get_sql(), query3.get_sql(), query4.get_sql(), query5.get_sql()