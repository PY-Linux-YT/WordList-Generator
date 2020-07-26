import itertools, os, sys, time
fm = "\033[1;34m[\033[1;35m+\033[1;34m]"

fm1 ="\033[1;31m[\033[1;32m+\033[1;31m]"
os.system("clear")
print""
print""
print ""
print"\033[1;91m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print""
print""
chrs=raw_input(fm +"\033[1;93mPlease Enter Here All Word for combination :>> \033[1;36m")
print ""
l=int(raw_input(fm +"\033[1;93mPlease Enter Minimum Lenth Of Words  : >>\033[1;36m  "))
k = l
print ""
j=int(raw_input(fm +"\033[1;93mPlease Enter Maximum Lenth Of Words  : >>\033[1;36m  "))
n = j+1
print ""
mtl=len(chrs)
p=[]
zt = raw_input(fm1 +"\033[1;93mPlease Enter Here Name Of Wordlist File :>> \033[1;36m")
print""
for ltp in xrange(k, n):
 ans=mtl**ltp
 p.append(ans)
tline=sum(p)
print fm1 +"\033[1;93mNumbers Of Total Lines : ", tline
print""
raw_input(fm1 +"\033[1;93m Are You Ready ?[Press Enter]")
print"\033[1;92m "

time1=time.asctime()
start=time.time()

psd = open(zt, 'a')
for i in xrange(k,n):
  r=i*100/n
  l=str(r)+' percent '
  sys.stdout.write("\r%s" % l)
  sys.stdout.flush()
  psd.flush()
  for xs in itertools.product(chrs, repeat=i):
    psd.write(''.join(xs)+'\n')
psd.flush()    
psd.close()

sys.stdout.write("\rDone Sucessfully")
os.system("clear")
print""
print""
print""
print""
print""
print"\033[1;91m====================================================================="
print "\033[1;92m                          Process Reports"
print""
print""
print" "+fm +"Process Started        \033[1;93m              : \033[1;95m", time1
end=time.time()
print" "+fm +"Process Completed  \033[1;93m                  : \033[1;95m", time.asctime()
totaltime=end-start
print" "+fm +"Total Time Consumed         \033[1;93m         :\033[1;95m ", totaltime, 'second'
rate=tline/totaltime
print" "+fm +"Rate Of Words Generating Per Seconds \033[1;93m:\033[1;95m ", rate 
print"\033[1;91m======================================================================"
print

print" \033[1;93m                 Subscribe PY-Linux in Youtube"
print ""
raw_input(fm +"\033[1;36mPress Enter For Exit")
os.system("clear && login")
