import subprocess

print("Which directory you want to visit:")
print("1:Downloads\n2:Friends\n3:Game of thrones\n4:Breaking bad\n5:The flash\n6:Music\n7:College\n8:Github repo\n9:Python programs\n")

s = int(input())

if s == 1:
	subprocess.Popen('explorer "C:\\Users\\Riz1_9wab\\Downloads"')	
	exit()
elif s == 2:
	subprocess.Popen('explorer "F:\\1.TV Series\\Friends"')
	exit()
elif s == 3:
	subprocess.Popen('explorer "F:\\1.TV Series\\Game of thrones"')
	exit()
elif s == 4:
	subprocess.Popen('explorer "E:\\1.Movies,Series\\Breaking bad"')
	exit()
elif s == 5:
	subprocess.Popen('explorer "E:\\1.Movies,Series\\The Flash"')
	exit()
elif s == 6:
	subprocess.Popen('explorer "E:\Music"')
	exit()
elif s == 7:
	subprocess.Popen('explorer "E:\College"')
	exit()
elif s == 8:
	subprocess.Popen('explorer "G:\githubrepo"')
	exit()
elif s == 9:
	subprocess.Popen('explorer "G:\Python programs"')
	exit()
else:
	print("Wrong choice")	


	