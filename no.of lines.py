myfile=open(r'C:\Users\pc\Desktop\Python programs\Poem.txt','r')
s=myfile.readlines()
linecount=len(s)
print("No.of lines in Poem.txt",linecount)
myfile.close()

# Optimized way to that
with open("C:\Users\pc\Desktop\Python programs\Poem.txt",'r') as fs:
  s = fs.realines()
  print(f"Number of lines in poem.txt are {len(s)}")
  
