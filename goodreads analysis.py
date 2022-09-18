import json

#open json data into read mode - first key is userdata and will throw an error code otherwise
with open(r'C:\Users\dange\Desktop\Goodreads-Analysis_Code-Lou\track_book_origins.json') as f:
    posts_json = json.load(f)

type(posts_json)
