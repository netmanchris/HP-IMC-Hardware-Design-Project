
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
import os, json, sys, time, subprocess, csv, time, datetime
from subprocess import call



#This section initialises the global variables
plat_nodes = 0
plat_col_units = 0
plat_operators = 0
plat_os = ""

#This section collects responses from the user to calculate the IMC Base Platform Requirements
'''===========================================================================================

=============================================================================================='''
def gather_plat_req():
        '''Called by _main_ function and will call the various gathering functions.'''
        global plat_nodes, plat_col_units, plat_operators, plat_os
        print ('''\n\n==============\n\nThis section will gather information specific to the HP IMC Platform.\n Other IMC modules will be covered in a future version of this tool\n\n==============''')
        plat_os = get_plat_os()     #See get_plat_os function for more info
        plat_operators = get_plat_operators()
        get_single_dev()    #see get_single_dev function for more info.
        get_stack_dev()
        get_server_dev()
        
        print('\n\n==============\n\nTotal nodes is : ' + str(plat_nodes))
        print ("Total collection units calculated is is: "+ str(plat_col_units))
        print("Total concurrent operators is " +str(plat_operators)+'\n\n==============\n\n')
        return plat_operators, plat_col_units, plat_nodes, plat_os

#Error Handling for Initial Questions
'''===========================================================================================

=============================================================================================='''
def get_plat_os():
        '''This function is called by the gather_plat_req function and is used to gather platform OS information from user.'''
        plat_os = input('What Operating System do you intend to use:\n1)Red Hat Enterprise Linux\n2)Windows\n :')
        if plat_os == '1':
             plat_os = "Linux"
             return plat_os
        elif plat_os == '2':
             plat_os = "Windows"
             return plat_os
        elif plat_os != '1' or plat_os != '2':
            print("Error: You must select an operating system")
            time.sleep(3)
            print ('\n'*80)
            get_plat_os()            
        elif plat_os == '':
            print("Error: You must select an operating system")
            time.sleep(3)
            print ('\n'*80)
            get_plat_os()        

def get_plat_operators():   #gather platform operator numbers
    '''This function is called by the gather_plat_req function and is used to gather number of IMC platform operators information from user.'''    
    plat_operators = input('\n\n==============\n\nWhat is the expected number of concurrent online operators?\n(This must be a value betwen 1 and 50)\n: ')
    if plat_operators == '':
        print("Error: You've input a invalid number.\nPlease Select a value between 1 and 50")
        time.sleep(2)
        print('\n'*80)
        get_plat_operators()
    elif is_number(plat_operators) == False:
        print("Error: You've input an invalid number.\nPlease select a value between 1 and 50")
        time.sleep(2)
        print('\n'*80)
        get_plat_operators()
    elif int(plat_operators) >50:
        print("Error: You've exceeded the maximum of a single system\nPlease Select a value between 1 and 50")
        time.sleep(2)
        print ('\n'*80)
        get_plat_operators()   
    elif int(plat_operators) < 1:
        print("Error: You've input a invalid number.\nPlease Select a value between 1 and 50")
        time.sleep(2)
        print('\n'*80)
        get_plat_operators()
    else:
        print('\n'*80)
        return plat_operators

def get_single_dev():
    '''This function is called by the gather_plat_req function and is used to gather single device information from user.'''    
    single_dev = input('\n\n==============\n\nDo you want to manage single network devices?\nThis includes routers, wireless controllers, and non-stacked switches\nY/N: ')
    if single_dev == '':
        print("Error Invalid Input.\nPlease select Y or N.")
        time.sleep(2)
        print('\n'*80)
        get_single_dev()
    if is_number(single_dev) == True:
        print ("Error Invalid Input.\nPlease select Y or N.")
        time.sleep(2)
        print ('\n'*80)
        get_single_dev()
    elif single_dev == "N" or single_dev == "n":
        print ('\n'*80)
        return          
    elif single_dev == "Y" or single_dev == "y":
        print('\n'*80)    
        SingleDevices()
    elif is_string(single_dev) == True:
        print("Error Invalid Input.\nPlease select Y or N.")
        time.sleep(2)
        print('\n'*80)
        get_single_dev()

def get_stack_dev():
    '''This function is called by the gather_plat_req function and is used to gather stack device information from user.'''    
    stack_dev = input('''\n\n==============\n\nDo you want to manage stacked network devices.\nThis includes devices managed as a single logical unit such as HP's IRF or Meshed Stacking technologies.\nY/N: ''')
    if stack_dev == '':
        print("Error Invalid Input.\nPlease select Y or N.")
        time.sleep(2)
        print('\n'*80)
        get_stack_dev()
    if is_number(stack_dev) == True:
        print ("Error Invalid Input.\nPlease select Y or N.")
        time.sleep(2)
        print ('\n'*80)
        get_stack_dev()
    elif stack_dev == "N" or stack_dev == "n":
        print ('\n'*80)
        return          
    elif stack_dev == "Y" or stack_dev == "y":
        print('\n'*80)
        StackDevices()
    elif is_string(stack_dev) == True:
        print("Error Invalid Input.\nPlease select Y or N.")
        time.sleep(2)
        print('\n'*80)
        get_stack_dev()

def get_server_dev():
    '''This function is called by the gather_plat_req function and is used to gather server device information from user.'''    
    server_dev = input('\n\n==============\n\nDo you want to monitor SNMP configured servers?\nY/N: ')
    if server_dev == '':
        print("Error Invalid Input.\nPlease select Y or N.")
        time.sleep(2)
        print('\n'*80)
        get_server_dev()
    if is_number(server_dev) == True:
        print ("Error Invalid Input.\nPlease select Y or N.")
        time.sleep(2)
        print ('\n'*80)
        get_server_dev()
    elif server_dev == "N" or server_dev == "n":
        print ('\n'*80)
        return          
    elif server_dev == "Y" or server_dev == "y":
        print('\n'*80)
        ServerDevices()
    elif is_string(server_dev) == True:
        print("Error Invalid Input.\nPlease select Y or N.")
        time.sleep(2)
        print('\n'*80)
        get_server_dev()

#Gather Stacked device management requirements
'''===========================================================================================

=============================================================================================='''        
def StackDevices():
       '''This function will gather input from the user and calculate the number of nodes and collection units consumed by the stacked network devices''' 
       global plat_nodes, plat_col_units
       print ("\n\n==============\n\nStacked Network Device Section:\n This section deals with stacked network devices such as HP Meshed stacking or IRF devices\n\n==============")
       stack_count = get_stack_count()
       print('\n'*80)
       stack_devices = get_stack_units()
       print('\n'*80)
       number_of_interfaces = get_interface_count()
       print('\n'*80)
       number_of_monitors = get_monitors_count()
       print('\n'*80)
       poll_interval = get_poll_interval()
       print('\n'*80)
       cpu = (1*stack_devices)
       memory = int(1*stack_devices)
       reachability = int(1)
       response_time = int(1)
       total_instances = int( (number_of_interfaces * number_of_monitors ) + cpu + memory +reachability + response_time)
       polled_units = int(stack_count*total_instances)
       stack_units = int(polled_units*(5/poll_interval))
       plat_col_units = ( plat_col_units + stack_units )
       plat_nodes = (plat_nodes + stack_count)
       if int(plat_nodes) > 15000:
              print ("Error: You've exceeded the maximum number of nodes on a single HP IMC system.\nPlease Consider a Hierarchical Deployment with no more than 15000 nodes per system.\nEnding Sizing Calculator Now.")
              sleep.time(5)
              quit()
       else:
              return plat_col_units, plat_nodes

def get_stack_count():
    stack_count = (input("\n\n==============\n\nWhat is the total number of network Stacks you want to monitor?\n: "))
    if stack_count == '':
        print("You must input a number between 1 and 15000")
        time.sleep(2)
        print('\n'*80)
        get_stack_count()
    elif is_number(stack_count) == False:
        print ("You must input a number between 1 and 15000")
        time.sleep(2)
        print('\n'*80)
        get_stack_count()
    elif int(stack_count) > 15000 or int(stack_count) < 1:
        print('You have exceeded the maximum capabilities of a single IMC system.\n Please consider a hierarchical design.')
        time.sleep(10)
        get_stack_count
    else:
        stack_count = int(stack_count)
        return stack_count

def get_stack_units():
    '''This function wil gather the number of units in a stack.'''
    stack_devices= input('''\n\n==============\nWhat is the average number of switches in a stack?\nIf unknown, please input a default value of "4".\n: ''')
    if stack_devices == '':
        print("You must input a number between 1 and 10")
        time.sleep(2)
        print('\n'*80)
        get_stack_units()
    elif is_number(stack_devices) == False:
        print ("You must input a number between 1 and 10")
        time.sleep(2)
        print('\n'*80)
        get_stack_units()
    elif int(stack_devices) > 10:
        print ("You must input a number between 1 and 10")
        time.sleep(2)
        print('\n'*80)
        get_stack_units()    
    else:
        stack_devices = int(stack_devices)
        type(stack_devices)
        return stack_devices


#Gather Server Management Requirements Section
'''===========================================================================================

=============================================================================================='''
def ServerDevices():
       global plat_nodes, plat_col_units
       print ("\n\n==============\n\nServer Device Section:\n This section deals with server devices which have been configured with SNMP\n\n==============")
       server_devices = get_server_count()
       print('\n'*80)
       proc_quantity = get_proc_quant()
       print('\n'*80)
       cores_quantity = get_cores_quant()
       print('\n'*80)
       num_drives = get_drives_quant()
       print('\n'*80)
       number_of_interfaces = get_interface_count()
       print('\n'*80)
       number_of_monitors = get_monitors_count()
       print('\n'*80)
       poll_interval = get_poll_interval()
       print('\n'*80)
       cpu = (1*(proc_quantity*cores_quantity))
       memory = (1)
       reachability = (1)
       response_time = (1)
       total_instances = int( (number_of_interfaces  ) + cpu + memory +reachability + response_time+num_drives)
       polled_units = int(server_devices*total_instances)
       server_col_units =  int(polled_units*(5/poll_interval))
       plat_col_units = ( plat_col_units + server_col_units )
       plat_nodes = (plat_nodes + server_devices)
       if int(plat_nodes) > 15000:
              print ("Error: You've exceeded the maximum number of nodes on a single HP IMC system.\nPlease Consider a Hierarchical Deployment with no more than 15000 nodes per system.\nEnding Sizing Calculator Now.")
              sleep.time(5)
              quit()
       else:
              return plat_col_units, plat_nodes


def get_server_count():
    '''This function is called by the ServerDevices function and is used to calculate the total number of servers to be monitored.
        It will take a the user input and return the var server_devices.'''    
    server_devices = (input("\n\n==============\n\n\n\n==============\n\nWhat is the total number of Servers you want to monitor?\n: "))
    if server_devices == '':
        print("You must input a number between 1 and 15000")
        time.sleep(2)
        print('\n'*80)
        get_server_count()
    elif is_number(server_devices) == False or int(server_devices) < 1:
        print ("You must input a number between 1 and 15000")
        time.sleep(2)
        print('\n'*80)
        get_server_count()
    elif int(server_devices) > 15000 :
        print('You have exceeded the maximum capabilities of a single IMC system.\nYou may wish to consider a hierarchical design.\nPlease input a number between 1 and 15000: "')
        time.sleep(2)
        get_server_count()
    else:
        server_devices = int(server_devices)
        return server_devices

def get_proc_quant():
    '''This function is called by the ServerDevices function and is used to calculate the total number of physical CPUs to be monitored.
       It will take the user input and return the var proc_quanity.'''
    proc_quantity = (input('''\n\n==============\n\nWhat is the average number of physical CPUs per monitored server?\nIf unknown, please input a default value of "2"\n: '''))
    if proc_quantity == '':
        print("You must input a valid number.")
        time.sleep(2)
        print('\n'*80)
        get_proc_quant()
    elif is_number(proc_quantity) == False or int(proc_quantity) < 1:
        print ("You must input a valid number.")
        time.sleep(2)
        print('\n'*80)
        get_proc_quant()
    else:
        proc_quantity = int(proc_quantity)
        return proc_quantity

def get_cores_quant():
    '''This function is called by the ServerDevices function and is used to calculate the total number of cores per physical CPU to be monitored.
       It will take the user input and return the var cores_quantity'''
    cores_quantity = (input('''\n\n==============\n\nWhat is the average number of cores per physical processor?\nIf unknown, please input a default value of "8"\n: '''))
    if cores_quantity == '':
        print("You must input a valid number.")
        time.sleep(2)
        print('\n'*80)
        get_cores_quant()
    elif is_number(cores_quantity) == False or int(cores_quantity) < 1:
        print ("You must input a valid number.")
        time.sleep(2)
        print('\n'*80)
        get_cores_quant()
    else:
        cores_quantity = int(cores_quantity)
        return cores_quantity

def get_drives_quant():
    '''This function is called by the ServerDevices function and is used to calculate the total number of logical drives to be monitored per server.
       It will take user unput and return the var num_drives.'''
    num_drives = (input('''\n\n==============\n\nWhat is the average number of logical drives per monitored server\nIf unknown, please input a default value of "3"\n: '''))
    if num_drives == '':
        print("You must input a valid number.")
        time.sleep(2)
        print('\n'*80)
        get_drives_quant()
    elif is_number(num_drives) == False or int(num_drives) < 1:
        print ("You must input a valid number.")
        time.sleep(2)
        print('\n'*80)
        get_drives_quant()
    else:
        num_drives = int(num_drives)
        return num_drives

#Gather Single device management requirements
'''===========================================================================================

=============================================================================================='''
def SingleDevices():
       global plat_nodes, plat_col_units
       print ("\n\n==============\n\nNetwork Device Section:\n This section deals with SNMP configured network devices that you wish to manage.")
       single_devices= get_single_count()
       print('\n'*80)
       number_of_interfaces = get_interface_count()
       print('\n'*80)      
       number_of_monitors = get_monitors_count()
       print('\n'*80)
       poll_interval = get_poll_interval()
       print('\n'*80)
       cpu = (1)
       memory = (1)
       reachability = (1)
       response_time = (1)
       total_instances = int( (number_of_interfaces * number_of_monitors ) + cpu + memory +reachability + response_time)
       polled_units = int(single_devices*total_instances)
       single_dev_units = (polled_units*(5/poll_interval))
       plat_col_units = ( plat_col_units + single_dev_units )
       plat_nodes = (plat_nodes + single_devices)
       return plat_col_units, plat_nodes

def get_single_count():
    '''This function is called by the ServerDevices function and is used to calculate the total number of single devices to be monitored.
        It will take a the user input and return the var single_devices.'''    
    single_devices = input('''\n\n==============\n\nWhat is the total number of network devices you wish to monitor?\n: ''')
    if single_devices == '':
        print("You must input a number between 1 and 15000")
        time.sleep(2)
        print('\n'*80)
        get_single_count()
    elif is_number(single_devices) == False or int(single_devices) < 1:
        print ("You must input a number between 1 and 15000")
        time.sleep(2)
        print('\n'*80)
        get_single_count()
    elif int(single_devices) > 15000 :
        print('You have exceeded the maximum capabilities of a single IMC system.\nYou may wish to consider a hierarchical design.\nPlease input a number between 1 and 15000: "')
        time.sleep(2)
        get_server_count()
    else:
        single_devices = int(single_devices)
        return single_devices


#This section will import the HPIMCHardwareSchemes.csv file as list of dictionaries and compare the values collected above to provide hardware platform recommendations

def Plat_HW_Guidance():
            #import csv file as dictionary
            with open ('HPIMC_Plat_HardwareSchemes.csv') as csvfile:
                       reader = csv.DictReader(csvfile)
                       for i in reader:
                               if ('PLAT' == i['Module'] and
                                   plat_os == i['OS'] and
                                   int(plat_operators) <= int(i['Max. online operators']) and
                                   int(plat_nodes) <= int(i['Node count']) and
                                   int(plat_col_units)  <= int(i['Collection units'])):
                                   current_time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
                                   with open("Recommended_System.txt", "w") as text_file:
                                           print ('''HP IMC Platform Sizing Utility Output
                                                  \n+=================================================================+
                                                  \nDISCLAIMER:
                                                  \nThis tool is intended to help you calculate the hardware platform requirements for the HP IMC  platform.
                                                  \nIn the occurrence of a disagreement, the official HP product documentation will be considered as correct.
                                                  \nThis tool is provided as-is with no warranty expressed or implied.
                                                  \nThis tool is for HP Internal Use Only and should be considered restricted and confidential.
                                                  \n+=================================================================+'''
                                                  +'''\nTime of Creation: '''+current_time+ '''\n=================================================================
                                           \nBased on your inputs, we have calculated the following requirements:
                                           \n=================================================================
                                           \nTotal Number of Nodes: '''+str(plat_nodes)+'''
                                           \nTotal Number of Collection Units: '''+str(plat_col_units)+'''
                                           \nTotal Number of Online Operators: '''+str(plat_operators)+'''
                                           \nOperating System: '''+i['OS']+'''
                                           \n32 or 64 Bit: '''+i["Version"]+'''
                                           \n\n=================================================================
                                           \nBased on your stated requirements, the recommended hardware platform is as follows:
                                           \nCPU: '''+i["CPU (main frequency ? 2.0 GHz)"]+'''
                                           \nMemory: '''+i["Memory "]+'''
                                           \nHard Drive Space: '''+i["Disk space for data storage (imcDataDir)"] +'''
                                           \n=================================================================
                                           \nThe recommended platform has the following characteristics :
                                           \nMaximum Managed Nodes: '''+ i["Node count"]+ '''
                                           \nMaximum Collection Units: ''' + i["Collection units"]+'''
                                           \nMaximum Online Operators: ''' + i["Max. online operators"], file=text_file)
                                           break
                               else:
                                  continue
            print(" Please open the file Recommended_System.txt located in the same directory as the sizing tool")
            time.sleep(5)
            call("notepad Recommended_System.txt")
#test functions
def is_string(s):
    try:
        str(s)
        return True
    except ValueError:
        return False
def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def get_interface_count():
    '''Called by multiple functions. Gathers the number of ethernet interfaces to be monitored for a given device'''
    number_of_interfaces = input('''\n\n==============\n\nWhat is the average number of ethernet interfaces you want to monitor?\nIf unknown, please input a default value of "4".\n: ''')
    if number_of_interfaces == '':
        print("You must input a valid number of ethernet interfaces.")
        time.sleep(2)
        print('\n'*80)
        get_interface_count()
    elif is_number(number_of_interfaces) == False:
        print ("You must input a valid number of ethernet interfaces.")
        time.sleep(2)
        print('\n'*80)
        get_interface_count()
    else:
        number_of_interfaces = int(number_of_interfaces)
        return number_of_interfaces

def get_monitors_count():
    '''Called by multiple functions. Gathers the number of SNMP polled elementsto be monitored for a given device'''
    number_of_interfaces = input('''\n\n==============\n\nWhat is the average number of SNMP metrics you want to monitor per interface: \nIf unknown, please input a default value of "8"\n: ''')
    if number_of_interfaces == '':
        print("You must input a valid number of SNMP monitors per interfaces.")
        time.sleep(2)
        print('\n'*80)
        get_monitors_count()
    elif is_number(number_of_interfaces) == False or int(number_of_interfaces) < 1:
        print ("You must input a valid number of SNMP monitors per interfaces.")
        time.sleep(2)
        print('\n'*80)
        get_monitors_count()
    else:
        number_of_interfaces = int(number_of_interfaces)
        return number_of_interfaces

def get_poll_interval():
    '''Called by multiple functions. Gathers the time in minutes required between SNMP polls'''
    poll_interval = input('''\n\n==============\n\nWhat is the number of minutes the system should wait between SNMP polls of monitored interfaces?(in minutes)\nIf unknown, please input a default value of "5".\n: ''')
    if poll_interval == '':
        print("You must input a valid number of minutes to wait between SNMP device polls.")
        time.sleep(2)
        print('\n'*80)
        get_poll_interval()
    elif is_number(poll_interval) == False or int(poll_interval) < 1:
        print ("You must input a valid number of minutes to wait between SNMP device polls.")
        time.sleep(2)
        print('\n'*80)
        get_poll_interval()
    else:
        poll_interval = int(poll_interval)
        return poll_interval

def get_imc_plat_recommendations():
    imc_plat = input("\n\n==============\n\nWould you like to design a new HP IMC System?\n: ")
    if imc_plat == "Y" or imc_plat == "y":
        print ("\n" *80) 
        gather_plat_req()
        Plat_HW_Guidance()
    elif imc_plat == "N" or imc_plat == "n":
            quit()
    elif is_string(imc_plat) == True:
            print("Invalid Input: Please Retry.")
            time.sleep(2)
            get_imc_plat_recommendations()
    elif is_number(imc_plat) == True:
            print("Invalid Input: Please Retry.")
            time.sleep(2)
            get_imc_plat_recommendations()

#Defines the program to be run
            
def main():
    print ('''\n
  +------------------------------------------------------------------------+
  |     | +------------------------------------------------------+  |      |
  |     | |       HP IMC PLatform Hardware Sizing Utility        |  |      |
  |     | +------------------------------------------------------+  |      |
  |     | +-----------------------------------------------------+   |      |
  |     | |   This tool is intended to help you calculate the   |   |      |
  |     | |    hardware platform requirements for the HP IMC    |   |      |
  |     | |                      platform.                      |   |      |
  |     | |In the occurrence of a disagreement, the official HP |   |      |
  |     | |product documentation will be considered as correct. |   |      |
  |     | |    This tool is provided as-is with no warranty     |   |      |
  |     | |                expressed or implied.                |   |      |
  |     | | This tool is for HP Internal Use Only and should be |   |      |
  |     | |       considered restricted and confidential.       |   |      |
  |     | +-----------------------------------------------------+   |      |
  +------------------------------------------------------------------------+''')
    get_imc_plat_recommendations()
    print ("Thank you. Come Again.")
    time.sleep(5)
    quit()
        

    
    


if __name__ == "__main__":
    main()
