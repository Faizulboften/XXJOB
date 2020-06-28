import os,sys,time,base64

file = raw_input("\033[1;97mMASUKAN FILE:\033[1;92m ")
fileopen = open(file).read()
xmanz = base64.b64encode(fileopen)
xixi = "import base64\nexec(base64.b64encode("+xmanz+"))"
cyka = file.replace(".py","c.py")
buka = open(cyka,"w")
buka.write(xixi)
buka.close()
print "\033[1;97mHASIL:\033[1;92m ",cyka
