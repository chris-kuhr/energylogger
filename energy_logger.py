#!/usr/bin/python3.2

'''
Created on 05.06.2014

@author: christoph
'''
import os
from twill.commands import *
import time as time
import urllib2

# Energenie Password                  
password = "" 

# Energenie IP Address
ip_addr = ""

login_url= "http://%s/login.html" % ip_addr
logger_url = "http://%s/energenie.html" % ip_addr

def login():
    
    go(login_url)
    fv("1", "pw", password)
    submit("0")
    
    
def get_data():           
    log_file = open("energy.log", "a")
    aResp = urllib2.urlopen(logger_url);
    energy_data_log_webpage = aResp.read();
                    
    log_vars = energy_data_log_webpage.split("var")
    
    for i, v in enumerate(log_vars):
        v1 = v.split("=")
        v2 = v1[1].split(";")
#	print v        
        if(i==10):
            log_voltage = float(float(v2[0])/10)
        elif(i==11):
            log_current = float(float(v2[0])/100)
        elif(i==12):
            log_power = float(float(v2[0])/100)
        elif(i==13):
            log_energy = float(float(v2[0])/1000)
     
    ttime = time.localtime()
    log_string = "%s.%s.%s-%s:%s:%s;%sV;%sA;%sW;%skWh;\n" %(ttime[2],ttime[1],ttime[0],ttime[3],ttime[4],ttime[5],log_voltage,log_current,log_power,log_energy)
#    print log_string     
    log_file.write(log_string)    
    log_file.close()
        
if __name__ == "__main__":
    login()
    while(1):
        time.sleep(10)
#	login()
        get_data()
        
