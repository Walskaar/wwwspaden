
import sys
import os
import threading
import time,sys
# import wget
print
print"WWW SPADEN"
print"Digging into the web"
time.sleep(1)                                      
print                                                                                  
print "Starting"
time.sleep(3)
os.system("wget --no-verbose -r --random-wait -c --secure-protocol=auto --mirror -e robots=off -U --server-response --progress=dot --show-progress --input-file=url.txt -x --force-directories --warc-file=sites  --no-warc-compression "   )
print
time.sleep(1)
print "Download Done"
