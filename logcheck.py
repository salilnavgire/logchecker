import os
import os.path
from glob import glob
import os.path
import re
#os.chdir("C:\Users\Salil\Desktop\done\Ninach23")
#sys.argv[1] = "C:\Users\Salil\Desktop\done\Ninach23"


count = 0
count1 = 0
found = 0


#checks for each file from subdirectories in the given path
for dirpath, dirnames, filenames in os.walk("C:\Users\Salil\Desktop\data"):
    for filename in [f for f in filenames if f.endswith(".txt")]:       
        os.chdir(dirpath)

#open file an check for patterns
	with open(str(filename)) as f:
		lines=f.readlines()
		count = 0
		count1 = 0
		found = 0
		count2 = 0

		#Checks for the string 'User' and counts the instances
		for w in range (0,len(lines)):
			if lines[w].find ('User') != -1:
				count = count + 1

		#Faulty logs have 'User' instance more than once
		#so print the path of the file and number of times the string is repeated
		if count > 1:
				print os.path.join(dirpath, filename)
				print "User-agent repeated",count,"times"

		#Following is a sample table entries from the log file
		#x	y	Ts		Events
		#196	73	2788		touch
		#190	75	2851		move
		#183	76	2867		move
		#139	-16	1364		move
		#124					move
		#negative and blank entries are errors
		for w in range (0,len(lines)):
			#check patterns using regular expressions
			match = re.search(r'^\d*\t', lines[w])
			if match:
				match1 = re.search(r'^\d+\t+\d+\t+\d+\t+\w*$', lines[w])
				if match1:
					pass
				else:
					count1 = count1 + 1
					a=(lines[w].split('	'))

					match1 = re.search(r'-\d+', lines[w])
					if match1:
						count2 = count2 +1

		#print number of blanks detected
		if (count1-count2) > 0:
			if count1 > 1:
				print os.path.join(dirpath, filename)
				print "'  ' detected",count1-count2,"times"

		#print the number of negative instances detected
		if count2 > 0:
			print os.path.join(dirpath, filename)
			print "negative ",count2,"times"


			
			
