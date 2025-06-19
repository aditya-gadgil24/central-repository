# Shree Ganeshay Namah

# json data formats
# pandas module functions for json

# code 01
import pandas as pd
js_dict = '[{'item' : 'gold', 'price' : 1025}, {'item' : 'silver', 'price' : 870}]'
newjs = pd.read_json(js_dict)
print(newjs)
# end of code