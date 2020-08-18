'''
AUTHOR: John Chavis 
DATE: 2020-MAY-25
NAME: convertCMatrix.py
DESC: This script will go through each model and create a 1-D matrix of the parameters and likelihood
	The first two paramters are the #number of columns and rows 
	#oRder of columns
	1) Likelihood of model 
	2) Paramter 1 
	3) Parameter 2 
	4) Paramter N
'''

import sys 
import os


gscDir = 'goldStandardChains/'

def main():
	#Grab argumetns
	nArgs = len(sys.argv)

	#FInd max param of model Maxparam 
	maxParam = 0 


	if nArgs == 1: 
		print('Please include number of Models in Command Line.')
	else:
		#graph numbre of models
		nModel = int(sys.argv[1])

		#Go into each folder and grab the chains here#
		for k in range(nModel): 
			#Grab all files 
			path = '{}model{}'.format(gscDir, k)
			fileList = [f for f in os.listdir(path)  if os.path.isfile(os.path.join(path,f))]

			#Grab all proper files-i.e. the ones with just paremtrs ad likelihood
			properFileList = [f for f in fileList if 'GSC' in f]


			for fileName in properFileList:
				#Open file 
				f = open('{}model{}/{}'.format(gscDir,k,fileName), 'r')

				#Grab chain number 
				chain = int(fileName.split('GSC')[1][0])


				#read off header 
				columns = f.readline().strip().split(',')

				#print(columns)

				#Figure out where column starts collect Likeihood
				#Figure out where logModle is is 
				stopIndx = columns.index('logModel')
				#print(stopIndx)

				#Check patmers (this is stopIndx -1)
				maxParam = max(maxParam, stopIndx )
				#FInd Totla numerb of lines 
				#And collect paramters
				res = []
				count = 0 
				for line in f.readlines():
					line = line.strip().split(',')
					count += 1 

					tmp = []
					
					tmp.append(float(line[stopIndx]))

					for i in range(stopIndx):
						tmp.append(float(line[i]))


					res.append(tmp[:])

					tmp[:] = []

				#print(res)

				#Write file 
				g = open('{}model{}/gsc{}.csv'.format(gscDir, k,chain), 'w')
				#Write total count and column number 
				g.write('{}\n{}\n'.format(count, stopIndx+1))
				for data in res: 
					for ele in data:
						#if ele != len(data):
						#	g.write('{},'.format(ele))
						#else:
						#	g.write('{}\n'.format(ele))
						g.write('{}\n'.format(ele))
				g.close()

				res[:] = []


				f.close()

		#Write out the max param so shell script can use 
		#print(maxParam)
		sys.stdout.write(str(maxParam))

main()
