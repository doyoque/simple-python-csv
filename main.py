import json
import pandas as pd

nama_file = 'output'
input_json = 'juraganhelm.json'

data = open(input_json, encoding = "utf-8").read()
data = data.replace("\n", "")

a = json.loads(data)

#assign GraphImages array
v = a["GraphImages"]

#reserve a empty array to be append
res = []
for x in v: #iterate the the array of GraphImage
    for h in x["comments"]["data"]: #iterate the array of data
        res.append({"username" : h["owner"]["username"], "comments" : h["text"]}) #append the value of "username" and "text"

pd.DataFrame(res).to_csv(nama_file + ".csv", index = False, encoding = "utf-8")
