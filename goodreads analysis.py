import json

file_name = 'data/track_book_origins.json'
#open json data into read mode - first key is userdata and will throw an error code otherwise
with open(file_name, 'r', encoding="utf8") as f:
    json_data = json.load(f)

#check data type
print(type(json_data))

