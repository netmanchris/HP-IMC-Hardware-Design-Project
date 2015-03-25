
#   IMC Hardware Design Project 1.0
#  Chris Young a.k.a Darth
#
#Hewlett Packard Company    Revision 1.0
#
#Change History.... 3/19/15
#

#This series of functions is intended to help gather customer requirements and provide
#recommendations based on recommendations from HP R&D Hardware Schemes Guide

#This section imports required libraries
import os, json, sys, time, subprocess, csv, time
from subprocess import call

#This section initialises the global variables
plat_nodes = 0
plat_col_units = 0
plat_operators = 0
plat_os = ""

#This section collects responses from the user to calculate the IMC Base Platform Requirements

def gather_plat_req():
        global plat_nodes, plat_col_units, plat_operators, plat_os
        #plat_nodes = 0
        #plat_col_units = 0
        #plat_operators = 0
        print ('''\n\n==============\n\nThis section will gather information specific to the HP IMC Platform.\n Other IMC modules will be covered in a future version of this tool\n\n==============''')
        plat_os = input('What Operating System do you intend to use:\n1)Red Hat Enterprise Linux:\n2)Windows:\n')
        if plat_os == '1':
                        plat_os = "Linux"
        elif plat_os == '2':
                        plat_os = "Windows"
        plat_operators = input('\n\n==============\n\nWhat is the expected number of concurrent online operators?\n(This must be a value betwen 1 and 50)\n: ')
        single_dev = input('\n\n==============\n\nDo you want to manage single network devices?\nThis includes routers, wireless controllers, and non-stacked switches\nY/N: ')
        if single_dev == "Y" or single_dev == "y":
            SingleDevices()
        server_dev = input('\n\n==============\n\nDo you want to manage Servers? Y/N: ')
        if server_dev == "Y" or server_dev == "y":
            ServerDevices()
        stack_dev = input("\n\n==============\n\nDo you want to manage stacks of switches? Y/N: ")
        if stack_dev == "Y" or stack_dev == "y":
            StackDevices()
        print('\n\n==============\n\nTotal nodes is : ' + str(plat_nodes))
        print ("Total collection units calculated is is: "+ str(plat_col_units))
        print("Total concurrent operators is " +str(plat_operators)+'\n\n==============\n\n')
        return plat_operators, plat_col_units, plat_nodes, plat_os
        

def StackDevices():
       global plat_nodes, plat_col_units
       print ("\n\n==============\n\nStacked Network Device Section:\n This section deals with stacked network devices such as HP Meshed stacking or IRF devices\n\n==============")
       stack_count = int(input("\n\n==============\n\nWhat is the total number of network Stacks you want to monitor?\n: "))
       stack_devices= int(input("\n\n==============\n\What is the average number of switches in a stack?\n (If unknown, please input 4)\n:"))
       number_of_interfaces = int(input("\n\n==============\n\nWhat is the average number of interfaces you want to monitor per stack?\n (If unknown, please type 4)\n: "))
       number_of_monitors = int(input("\n\n==============\n\nWhat is the average number of SNMP metrics you want to monitor per interface: \n (If unknown please type 8)\n: "))
       cpu = int(1*stack_devices) 
       memory = int(1*stack_devices)
       reachability = int(1)
       response_time = int(1)
       total_instances = int( (number_of_interfaces * number_of_monitors ) + cpu + memory +reachability + response_time)
       polled_units = int(stack_count*total_instances)
       poll_interval = int(input("How many minutes should we wait between polling a device?(in minutes)\n(If unknown type 5)\n: "))
       stack_units = int(polled_units*(5/poll_interval))
       plat_col_units = ( plat_col_units + stack_units )
       plat_nodes = (plat_nodes + stack_count)
       return plat_col_units, plat_nodes

def ServerDevices():
       global plat_nodes, plat_col_units
       print ("\n\n==============\n\nServer Device Section:\n This section deals with server devices which have been configured with SNMP\n\n==============")
       server_devices = int(input("\n\n==============\n\nWhat is the total number of Servers you want to monitor?\n: "))
       proc_quantity = int(input("\n\n==============\n\nWhat is the average number of processors per monitored server?\n(If unknown please type 2)\n: "))
       cores_quantity = int(input("\n\n==============\n\nWhat is the average number of cores per processor?\n(If unknown please type 8)\n: "))
       num_drives = int(input("\n\n==============\n\nWhat is the average number of logical drives per monitored server\n(If unknown please type 3)\n: "))
       number_of_interfaces = int(input("\n\n==============\n\nWhat is the average number of network interfaces you want to monitor per monitored server?\n(If unknown please type 3)\n: "))
       number_of_monitors = int(input("\n\n==============\n\nWhat is the average number of SNMP metrics you want to monitor per interface: \n (If unknown please type 8)\n: "))
       cpu = (1*(proc_quantity*cores_quantity))
       memory = (1)
       reachability = (1)
       response_time = (1)
       total_instances = int( (number_of_interfaces  ) + cpu + memory +reachability + response_time+num_drives)
       polled_units = int(server_devices*total_instances)
       poll_interval = int(input("How many minutes should we wait between polling the servers?(in minutes)\n(If unknown type 5)\n: "))
       server_col_units =  int(polled_units*(5/poll_interval))
       plat_col_units = ( plat_col_units + server_col_units )
       plat_nodes = (plat_nodes + server_devices)
       return plat_col_units, plat_nodes
                

def SingleDevices():
       global plat_nodes, plat_col_units
       print ("\n\n==============\n\nNetwork Device Section:\n This section deals with network devices which you wish have been configured with SNMP\n\n==============")
       single_devices=int(input('''\n\n==============\n\nWhat is the total number of network devices you wish to monitor?\n: '''))
       number_of_interfaces = int(input("\n\n==============\n\nWhat is the average number of interfaces you want to monitor per device?\n(If unknown please type 2)\n: "))
       number_of_monitors = int(input("\n\n==============\n\nWhat is the avereage number of SNMP metrics you want to monitor per interface?\n(If unknown please type 8)\n: "))
       cpu = (1)
       memory = (1)
       reachability = (1)
       response_time = (1)
       total_instances = int( (number_of_interfaces * number_of_monitors ) + cpu + memory +reachability + response_time)
       polled_units = int(single_devices*total_instances)
       poll_interval = int(input("How many minutes should we wait between device poll?(in minutes)\n(If unknown type 5)\n: "))
       single_dev_units = (polled_units*(5/poll_interval))
       plat_col_units = ( plat_col_units + single_dev_units )
       plat_nodes = (plat_nodes + single_devices)
       return plat_col_units, plat_nodes

#This section will import the HPIMCHardwareSchemes.csv file as list of dictionaries and compare the values collected above to provide hardware platform recommendations

def Plat_HW_Guidance():
            global test_list
            test_list = None
            #import csv file as dictionary
            with open ('HPIMC_Plat_HardwareSchemes.csv') as csvfile:
                       reader = csv.DictReader(csvfile)
                       for i in reader:
                               if ('PLAT' == i['Module'] and
                                   plat_os == i['OS'] and
                                   int(plat_operators) <= int(i['Max. online operators']) and
                                   int(plat_nodes) <= int(i['Node count']) and
                                   int(plat_col_units)  <= int(i['Collection units'])):
                                       text_file = open("Recommended_System.txt", "w")
                                       #print (json.dumps(i, indent = 4), file=text_file)
                                       print ('''\n\n=================================================================\n
                                         \nBased on your inputs, we have calculated the following requirements:\n
                                         \n\n=================================================================\n
                                         \nTotal Number of Nodes: '''+str(plat_nodes)+'''
                                         \nTotal Number of Collection Units: '''+str(plat_col_units)+'''
                                         \nTotal Number of Online Operators: '''+str(plat_operators)+'''
                                         \nOperating System: '''+i['OS']+'''
                                         \n32 or 64 Bit: '''+i["Version"]+'''
                                         \n\n=================================================================\n
                                         \nBased on your stated requirements, the recommended hardware platform is as follows:\n
                                         \nCPU: '''+i["CPU (main frequency ? 2.0 GHz)"]+'''
                                         \nMemory: '''+i["Memory "]+'''
                                         \nHard Drive Space: '''+i["Disk space for data storage (imcDataDir)"] +'''\n\n
                                         \n\n=================================================================\n
                                         \nThe recommended platform has the following charecteristics:\n
                                         \nMaximum Managed Nodes: '''+ i["Node count"]+ '''\n
                                         \nMaximum Collection Units: ''' + i["Collection units"]+'''\n
                                         \nMaximum Online Operators: ''' + i["Max. online operators"], file=text_file)
                               else:
                                  continue
            text_file.close
            print(" Please open the file Recommended_System.txt located in the same directory as the sizing tool")
            #call("notepad Recommended_System.txt")
            #time.sleep(5)   

#Defines the program to be run
            
def main():
    print ('''\n\n==============\n\nThis tool is intended to help you identify the hardware requirements for your HP IMC Platform server.\n In the occurance of a disagreemnt, the most current HP documentation should be considered as correct. This tool and any recommendations are provided as is with no warranty, expressed or implied\n\nThis tool is for HP internal use only and should be considered restricted and confidential.\n\n==============''')    
    imc_plat = input("Is this a new install Y/N:")
    if imc_plat == "Y" or imc_plat == "y":
        gather_plat_req()
        Plat_HW_Guidance()
    
        

    
    


if __name__ == "__main__":
    main()
