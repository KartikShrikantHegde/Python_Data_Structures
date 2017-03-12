import os
for dirpath, files in os.walk("./TREE/"):
	for filename in files:
		fname = os.path.join(dirpath,filename)
		with open(fname) as myfile:
			print(myfile.read())