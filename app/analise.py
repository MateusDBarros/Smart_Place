import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import matplotlib.pyplot as plt



password = quote_plus("****")
engine = create_engine(f"postgresql+psycopg2://postgres:{password}@127.0.0.1:5432/smart_place")

query = """
    
SELECT
    p.name AS product_name,
    p.price AS unit_price,
    i.quantity AS quantity,
    (p.price * i.quantity) AS total_price,
    o.data AS time_data,
    o."tableNum_id" AS table_id
FROM api_itempedido i
JOIN api_order o ON i.pedido_id = o.id
JOIN api_product p ON i.product_id = p.id;


"""

query2 = 'SELECT * FROM api_product;'


df = pd.read_sql(query, con=engine)

print(df.head())
print(df.columns)


df.plot(x="product_name", y="total_price", kind="bar", title="Produtos mais vendidos")
plt.tight_layout()
plt.show()
