import os

def main():
	path="Dataset/kaggle/annotations"
	

	print "=====> [INFO] CHORD EXTRACTION STARTED... <===="

	for directory in os.listdir(path):
		if not directory.startswith("."):
			for file in os.listdir(path+"/"+directory):
				if ("inv.lab" in file) or ('7.lab' in file): 
					print "kkjn"
					os.remove(path+"/"+directory+"/"+file)


if __name__== "__main__":
	main()