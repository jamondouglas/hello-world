import ijson
import os
print(os.getcwd())


with open("src/my_first_app/files/practice_data.json","rb") as f:
	user_ids = [uid for uid in ijson.items(f,"users.item.id")]
	print(user_ids)