import json
import os
import pandas as pd

# assert isinstance(file)

def read_json(file_path):
    with open(file_path) as json_file:
        file = json.load(json_file)

    return file

def read_all_json_files(JSON_ROOT):
    dfs = []
    source = []

    for filename in os.listdir(JSON_ROOT):
        if filename.endswith(".json"):
            content = read_json(JSON_ROOT + filename)
            contents = pd.DataFrame(content['results'])
            contents['source'] = (filename)
            dfs.append(contents)
            source.append(filename)
    return pd.concat(dfs, ignore_index=True)

    df = read_all_json_files('./data/daily_summaries/')