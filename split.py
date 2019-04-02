import pandas as pd 

import shutil, os
files = '/home/quest/Pictures/udacity_driving_datasets'
for f in files:
    shutil.copy(f, 'dest_folder')
    

cv=pd.read_csv('/home/quest/trainsample.csv',delimiter=",")
print(cv['frame'])

for row in cv:
    for f in files:
        if cv['frame'][row]==f
            shutil.copy(f,'/home/quest/train')