import subprocess
import os
import signal

cmd = ['pgrep -f -l .*strandShiva.py']
process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, 
stderr=subprocess.PIPE)
my_pid, err = process.communicate()
#print("len(my_pid.splitlines())",my_pid.splitlines()[1])
print('my_pid',my_pid)
print('Number of python:',my_pid.count("python"))
print(my_pid.splitlines())
pyCount = my_pid.count("python")
my_pid_app = my_pid.splitlines()
strApp = []
for i in range(0,len(my_pid.splitlines())):
   if pyCount == 1:
      break
   strApp.append(my_pid_app[i].split())
   if strApp[i][1] == 'python':
      strd = 'sudo kill '+strApp[i][0]
      print(strd)
      os.system(strd) 
      pyCount = pyCount-1
      
print('End PyCount:',pyCount)

   
#os.killpg(int(my_pid.splitlines()[1]),signal.SIGTERM)





'''
if len(my_pid.splitlines()) >1:
   for i in range(0,(len(my_pid.splitlines())-3)):
       strd = 'sudo kill '+my_pid.splitlines()[i]
       print(strd)
       #os.system(strd) 
   #os.killpg(os.getpgid(process.pid ),signal.SIGTERM)
'''       

'''
   process.kill()
   process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
   my_pid, err = process.communicate()
   print("process:",my_pid)
'''
'''
   print("Running")

   exit()
else:
  print("Not Running")
'''
