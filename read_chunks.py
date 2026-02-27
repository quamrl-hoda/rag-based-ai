import requests
import os
import json   # ✅ must import
import pandas as pd
def create_embedding(text_list):
    r = requests.post(
        "http://localhost:11434/api/embed",
        json={
            "model": "bge-m3",
            "input": text_list
        }
    )
    return r.json()["embeddings"]
# a = create_embedding(["cat mat sat", "quamrul dance on the mat"])
# print(a)
# list JSON files
json_files = os.listdir("jsons") # list all the 
# print(json_files)
my_dict = []
chunk_id = 0

for json_file in json_files:
    with open(f"jsons/{json_file}") as f:
        content = json.load(f)   # ✅ correct
    print(f"creating embeddings for {json_file}")
    embeddings = create_embedding([c['text'] for c in content["chunks"]])
    
    for i, chunk in enumerate(content["chunks"]):
        chunk['chunk_id'] = chunk_id
        chunk['embedding'] = embeddings[i]
        chunk_id += 1
        my_dict.append(chunk)
    # break  # only first file
print(my_dict)
df = pd.DataFrame.from_records(my_dict)
print(df)