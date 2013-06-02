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


for dirpath, dirnames, filenames in os.walk("C:\Users\Salil\Desktop\data"):
    for filename in [f for f in filenames if f.endswith(".txt")]:
        #print os.path.join(dirpath, filename)
        #path = str(os.path.join(dirpath, filename))
        #print path
        os.chdir(dirpath)

        #print filename

  with open(str(filename)) as f:
		#pass
		#print "sal"
		lines=f.readlines()
		#print lines
		count = 0
		count1 = 0
		found = 0
		count2 = 0
		for w in range (0,len(lines)):
			if lines[w].find ('User') != -1:
				count = count + 1
			

		if count > 1:
				print os.path.join(dirpath, filename)
				print "User-agent repeated",count,"times"
				#print lines
			
		for w in range (0,len(lines)):
			#print lines[w]
			match = re.search(r'^\d*\t', lines[w])
			#print 'matching'
			if match:
				#print 'ok'
				match1 = re.search(r'^\d+\t+\d+\t+\d+\t+\w*$', lines[w])
				if match1:
					#print 'waaj'
					pass
				else:
					#print "waajaa"
					count1 = count1 + 1
					#print lines[w]
					a=(lines[w].split('	'))
					#print a[1]

					match1 = re.search(r'-\d+', lines[w])
					if match1:
						#print 'waaj'
						count2 = count2 +1
						#print a


		if (count1-count2) > 0:
			if count1 > 1:
				print os.path.join(dirpath, filename)
				print "'  ' detected",count1-count2,"times"
		if count2 > 0:
			print os.path.join(dirpath, filename)
			print "negative ",count2,"times"
			


			
			#print count1

			if lines[w].find ('x\ty\tTs\t\tEvents\n') != -1:
				#print 'man'
				pass
				#found++

