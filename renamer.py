import os
import glob
import gc

files = glob.glob('very_large_data/autism_data/autistic/*.mp4')
i = 1

for file in files:
	os.rename(file, str(i)+'.avi')
	i = i+1
	print('running on autistic data, file number '+ str(i)+'.avi')
	gc.collect()
