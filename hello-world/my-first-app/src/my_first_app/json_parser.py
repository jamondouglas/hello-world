import ijson
import os
print('cwd:  ',os.getcwd())

def parse_json_structure(file_path, max_events=50):
	with open(file_path,"rb") as f:
		should_print = True
		arr_length = 0
		for item in ijson.items(f, "data.item"):
			print(item[0])
			# print(len(item))
			# if not should_print:
			# 	break
			# dir(item)

			# last_item = item.
			# print(len(item))
			# print(dir(item))
			# should_print = False

def parse_json_structure_investigation(file_path, max_events=30):
	with open(file_path,"rb") as f:
		parser = ijson.parse(f)
		i=0
		for prefix, data_type, value in parser:
			if prefix.__contains__("meta"):
				continue
			if i >= max_events:
				break
			i += 1
			print(f"prefix: {prefix}, data_type: {data_type}, value: {value}")
		# for elems in ijson.items(f,"meta.view"):
		#
		# filtered_user = [user for user in users if user["age"] > 20]
		# print(filtered_user)
		# 	print(elems)

parse_json_structure("files/ev.json", 400)
# parse_json_structure_investigation("files/ev.json", 100)