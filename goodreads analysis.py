#import modules
import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#open json data into read mode - first key is userdata and will throw an error code otherwise
with open('data/track_book_origins_edit.json', 'r') as json_file:
    json_data = json.load(json_file)

print(type(json_data))

print(len(json_data))

#open json data into read mode - first key is userdata and will throw an error code otherwise
with open('data/activity_edit.json', 'r') as f:
    json_data_activity = json.load(f)

print(type(json_data_activity))

print(len(json_data_activity))



#create scatterplot visualization
#x = json_data.keys("created_at")
#y = json_data_activity.keys("activitytype")
#plt.scatter(x, y)
#plt.title('Goodreads Scatterplot')
#plt.xlabel('Dates')
#plt.ylabel('Books')

#plt.show()


