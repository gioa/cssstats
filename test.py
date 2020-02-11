from pathlib import Path
from collections import defaultdict
import itertools
import subprocess
import pandas 
import json
import glob

# directory = "/Users/joy/GitHub/mlflow/mlflow/server/js/src"
#output = './JSON'
# Path(output).mkdir(parents=True, exist_ok=True)

# Step 1: use CSSSTATS to generate json files of all the CSS declarations 
# pathlist = Path(directory).glob('**/*.css')
# for path in pathlist:
#      # because path is object not string
#      path_in_str = str(path)
#      print(output + path.stem + ".json")     
#      subprocess.run(["cssstats", path_in_str, output + "/" + path.stem + ".json"])

# Step 2: Calculate all the different declarations  
# def set_default(obj):
# 	if isinstance(obj, set):
# 		return list(obj)
# 	raise TypeError

dict_merge = defaultdict(list)

for f in Path('./JSON').glob("*.json"):             #here you will loop over multiple Json files
	with open(f, "r") as infile:
		json_text=json.load(infile)['declarations']['properties'] 

		for k, v in json_text.items():
			if v not in dict_merge[k]:
				dict_merge[k].append(v)

for k, v in dict_merge.items():
	v_2= list(itertools.chain(*v))	
	dict_merge[k] = list(set(v_2))
	print (k, dict_merge[k])

with open("merged_file.json", "w") as outfile:    #filling the resultant file with Jason content
     #json.dump(json.dumps(dict_merge, default=set_default), outfile)                 #json.dump will fill output file with merged data
     json.dump(dict_merge, outfile)                 #json.dump will fill output file with merged data


pandas.read_json('./merged_file.json',lines=True).to_csv('merged_file.csv')
# pathlist = Path(output).glob('*.json')
# for path in pathlist:
# 	path_in_str = str(path)
# 	print(path_in_str)
# 	with open(path) as f:
# 		json_text = json.load(f)
# 		#print (json_text['declarations']['properties'])
# 		df_total = df_total.append(pd.DataFrame(json_text['declarations']['properties']))
# 	print (df_total.head())

# npm i gulp-merge-json
#gulp.src('./JSON/**/*.json').pipe(merge()).pipe(gulp.dest('./dist'));

