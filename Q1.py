from datetime import datetime
from time import sleep

filepath = "C:\\Users\\VIGNESH B\\shell_scripts\\good.txt"
start = "starting nxengine"
run = "nxengine is running"
bool_var = True
#print("this pg exeecution start ", flush=True)
while(bool_var == True):
    #print("iterating the log file for " +  start , flush=True)
    file = open(filepath, "r");
    lines =file.readlines()
    #print(lines)
    #file.close()
    for line in lines:
      #print(line , flush=True)
      if(start in line):  
       #print(start)  
       bool_var = False 
       break 
    file.close()
#print(start)
bool_var = True
i=0
while(bool_var == True):
    file = open(filepath, "r");
    lines =file.readlines()
    #print(lines)
    for line in lines:
     if(run in line):  
       #print(run) 
       bool_var = False 
       break
    print("Start Cycle:" +str(i)+ " " + "Duration: " + datetime.now().strftime("%H:%M:%S"))   
    i=i+1
    file.close()
#print(run)