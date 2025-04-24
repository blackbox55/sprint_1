import pandas as pd
import numpy as np

"""
random_phrase function will print out a 
random phrase base on the  
parameters already provided!
"""


def random_phrase():
   adjectives =  ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']
   nouns =['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']
   noun = np.random.choice(nouns)
   adjective = np.random.choice(adjectives)
   return f'{adjective} {noun}'
random_phrase()

print(random_phrase())
print(random_phrase())
print(random_phrase())

"""
random_float will give a random float
ranging from 0 to 300!
"""

def random_float(min = 0, max = 300):
    score = np.random.uniform(min, max, 1)
    result = round(np.random.choice(score),2)
    return f'random result {result}'
random_float(7,500)

print(random_float())
print(random_float())
print(random_float())

"""
random_bowling_score will give
a random bowling score!
"""

def random_bowling_score(min = 0, max = 300):
    assert min == 0
    assert max == 300
    score = range(min, max, 1)
    result = np.random.choice(score)
    return f'bowling result is {result}'
random_bowling_score(0,300)
print(random_bowling_score())
print(random_bowling_score())


"""
silly_tuple will give
an adjective mixed with a noun, rating,
 and score!
"""

def silly_tuple(adj_n = None, star_rating = None, score = None):
   adj_n =  ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']
   nouns =['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']
   noun_index = np.random.randint(0,len(nouns))
   adj_index = np.random.randint(0,len(adj_n))
   noun = nouns[noun_index]
   adjective = adj_n[adj_index]
   star_rating = np.random.uniform(0, 5, 1)
   result = round(np.random.choice(star_rating),1)
   min = 0
   max = 300
   score = range(min, max, 1)
   res = np.random.choice(score)
   return adjective, noun, result, res

print(silly_tuple())
print(silly_tuple())
print(silly_tuple())


"""
silly_tuple_list will provide
a tuple within a list consisting of
the attributes above!
"""

def silly_tuple_list(adj_n = None, star_rating = None, score = None):
   adj_n =  ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']
   nouns =['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']
   noun = np.random.choice(nouns)
   adjective = np.random.choice(adj_n)
   star_rating = np.random.uniform(0, 5, 1)
   result = round(np.random.choice(star_rating),1)
   min_val = 0
   max_val = 300
   score = range(min_val, max_val, 1)
   res = np.random.choice(score)
   lis = []
   for i in range(3):
    lis.append(silly_tuple())
   return lis

print(silly_tuple_list())

"""
split_dates will split the dates of
a time-series dataframe
provide(df, target)
make sure your dates are parsed and passed
as an index!
objects will be preset in this format
train_df, val_df, test_df = value, value, value
"""

def split_dates(df = None, target_column = None):
  if df != None:
    yearly_proportions = df.index.year.value_counts(normalize=True)
    train_years = yearly_proportions[yearly_proportions.cumsum() <= 0.7].index.tolist()
    val_years = yearly_proportions[(yearly_proportions.cumsum() > 0.7) &(yearly_proportions.cumsum() <= 0.9)].index.tolist()
    test_years = yearly_proportions[yearly_proportions.cumsum() > 0.9].index.tolist()
  
      
    train_df = df[df.index.year.isin(train_years)]
    val_df = df[df.index.year.isin(val_years)]
    test_df = df[df.index.year.isin(test_years)]  
    return train_df, val_df, test_df

if __name__ == '__main__':
   pass