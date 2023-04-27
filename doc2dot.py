import os
import glob
import sys

PATH = sys.argv[1]
TARGET_EXTENSIONS = []
i = 2
while i<len(sys.argv):
    TARGET_EXTENSIONS.append(sys.argv[i])
    i = i + 1

print("Looking for files: ",end='')
for ext in TARGET_EXTENSIONS:
    print(" *."+ext,end='')
print("")

def rrun(folder):
    print(folder)
    rlist = []
    if folder[0]!='.':
        insider = os.listdir(folder)
        for subitem in insider:
            if os.path.isfile(folder+"/"+subitem):
                print("\t"+subitem)
                extension = subitem.split('.')[-1]
                if extension!='mk':
                    rlist.append(folder+"/"+subitem)
            if os.path.isdir(folder+"/"+subitem):
                if subitem[0]!='.':
                    rrlist = rrun(folder+"/"+subitem)
                    for sitem in rrlist:
                        rlist.append(sitem)
    return(rlist)

def edgefinder(rlist,file,targets):
    # file -> where it's looking for
    # item -> what it's looking for
    ext = file.split('.')[-1]
    if ext in targets:            
        for item in rlist:
            f = open(file,"r")
            filename = item.split('/')[-1]
            print("Looking for string: "+filename+" in file: "+file)
            try:
                if f.read().find(filename)>0:
                    print("\t\""+file+"\" -> \""+item+"\"",file=sys.stderr)
                    print("Link found")
            except:
                print("ERROR in file: "+file)
            f.close()
                

rlist = rrun(PATH)
print("=======================================================")
print("digraph "+PATH.split('/')[0],file=sys.stderr)
print("{",file=sys.stderr)
for item in rlist:
    edgefinder(rlist,item,TARGET_EXTENSIONS)
print("}",file=sys.stderr)