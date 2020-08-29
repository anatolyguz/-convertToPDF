from sys import platform


# path = '/home/user/Instructions'
path = 'C:\\Instructions'


# def convertmht(path, file):
# 	infile = path+'/'+file;
# 	outfile = path+'/'+'Instruction.pdf';
# 	pdfkit.from_file(infile, outfile)

def convertdoc(path, file):
	infile = path+'\\'+file;
	outfile = path+'\\'+'Instruction.pdf';
	convert(infile, outfile)


def osPatform():
	return platform
	# if platform == "linux" or platform == "linux2":
	#    	# linux
	# elif platform == "darwin":
	#    	# OS X
	# elif platform == "win32":
	#    	# Windows...



def filesbypass(path, level=1):
	# print('Level = ', level, 'Content:', os.listdir(path))
	for i in os.listdir(path):
		if os.path.isdir(path+'\\'+i):
			# print('down to.... ', path+'/'+i)
			filesbypass(path+'\\'+i,level+1)
			# print('up from... ', path)
		else:
			print(path+'\\'+i)
			filename, file_extension = os.path.splitext(path+'/'+i)
			print(file_extension)
			# if file_extension == '.mht':
			# 	cconvertmht(path, i)
			if file_extension == '.doc' or file_extension == '.docx':
				convertdoc(path, i)


print(osPatform())

