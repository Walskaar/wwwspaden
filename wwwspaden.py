
import sys
import os
import threading
import time,sys
# import wget
print
print"/$$      /$$/$$      /$$/$$      /$$        /$$$$$$ /$$$$$$$  /$$$$$$ /$$$$$$$ /$$$$$$$$/$$   /$$"
print"| $$  /$ | $| $$  /$ | $| $$  /$ | $$       /$$__  $| $$__  $$/$$__  $| $$__  $| $$_____| $$$ | $$"
print"| $$ /$$$| $| $$ /$$$| $| $$ /$$$| $$      | $$  \__| $$  \ $| $$  \ $| $$  \ $| $$     | $$$$| $$"
print"| $$/$$ $$ $| $$/$$ $$ $| $$/$$ $$ $$      |  $$$$$$| $$$$$$$| $$$$$$$| $$  | $| $$$$$  | $$ $$ $$"
print"| $$/   \  $| $$/   \  $| $$/   \  $$      |  $$$$$$| $$     | $$  | $| $$$$$$$| $$$$$$$| $$ \  $$"
print"|__/     \__|__/     \__|__/     \__/       \______/|__/     |__/  |__|_______/|________|__/  \__/"
print"Updated 15.01.2021"
print"Digging into the web"
time.sleep(1)                                      
print                                                                                  
print "Starting"
time.sleep(3)
os.system("wget --no-verbose -r --random-wait -c --secure-protocol=auto --mirror -e robots=off -U --server-response --progress=dot --show-progress --input-file=url.txt -x --force-directories --warc-file=sites "   )
os.system ("mv sites.warc.gz wwww.sites.warc.gz")
print
time.sleep(1)
print "Done"