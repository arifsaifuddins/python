# create, read, write file

myFile = open('basic/files/docs.txt', 'w')

print(myFile.name)
print(myFile.mode)

myFile.write('testing')
myFile.write(' testing2')
myFile.close()

myFile = open('basic/files/docs.txt', 'r+')
print(myFile.read(100))
