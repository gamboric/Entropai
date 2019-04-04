#automatic_harvest_data.py

import os



def list_filepaths():
	f = []
	path ="../video_data/"
	listdir= os.listdir(path)

	for dirr in listdir:
		pathdir = path+str(dirr) + '/'

		if os.path.isdir(pathdir):

			for file in os.listdir(pathdir):
				filepath = pathdir+str(file)

				f.append(filepath)
	return f


f = list_filepaths()

for file in f:
	command = "python2 ./processings.py "+ str(file)
	os.system("bash -c '%s'" %command)
