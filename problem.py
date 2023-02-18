import itertools
import pandas as pd


df = pd.DataFrame({
    'group1': [1, 2, 2, 3, 3, 3, 4],
    'group2': ['A', 'A', 'B', 'B', 'C', 'C', 'C'],
    'value1': [1, 2, 4, 1, 3, 1, 2],
    'value2': [5, 6, 7, 8, 9, 10, 11]
})

group_sequence = list(itertools.product(df['group1'], df['group2']))

groups = df.groupby(['group1', 'group2']).sum().reindex(group_sequence, fill_value=0)

print(groups)