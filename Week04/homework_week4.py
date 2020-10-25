import pandas as pd
import numpy as np

names = ['kangkang', 'hanmeimei', 'lilei', 'jane']
ages = [22, 33, 44, 55]
indexs = [i for i in np.random.randint(0, len(names), 20)]
table = pd.DataFrame({
    'id': [i for i in range(20)],
    'name': [names[x] for x in indexs],
    'age': [ages[x] for x in indexs],
    'order_id': [i for i in np.random.randint(0, 6, 20)]
})

table1 = pd.DataFrame({
    'id': [i for i in range(20)],
    'name': [names[x] for x in indexs]
})

table2 = pd.DataFrame({
    'id': [i for i in range(10)],
    'order_id': [i for i in np.random.randint(1, 20, 10)]
})

# 1. SELECT * FROM data;
table

# 2. SELECT * FROM data LIMIT 10;
table.head(10)

# 3. SELECT id FROM data;  //id 是 data 表的特定一列
table['id']

# 4. SELECT COUNT(id) FROM data;
table['id'].count()

# 5. SELECT * FROM data WHERE id<1000 AND age>30;
table[ (table['id'] < 1000) & (table['age'] > 30) ]

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
table1.groupby('id').size()   

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
pd.merge(table1, table2, on='id', how='inner') 

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
pd.concat([table1, table2])

# 9. DELETE FROM table1 WHERE id=10;
table1[ table['id'] != 10 ] 

# 10. ALTER TABLE table1 DROP COLUMN column_name;
table1.drop(columns='name')