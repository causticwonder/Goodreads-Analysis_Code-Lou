import json

#open json data into read mode - first key is userdata and will throw an error code otherwise
with open('data/track_book_origins_edit.json', 'r') as f:
    json_data = json.load(f)

print(type(json_data))

print(len(json_data))


