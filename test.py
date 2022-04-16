import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
arquivo1 = os.path.join(dir_path,"arquivo_test.txt")
arquivo2 = os.path.join(dir_path,"arquivo2.txt")

f = open(arquivo1, "r")
print(arquivo1)
print(f.readline())


f = open(arquivo2, "r")
print(arquivo2)
print(f.readline())
