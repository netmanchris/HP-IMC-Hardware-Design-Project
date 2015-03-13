
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
import os, json, sys, time, subprocess, csv

#This section initialises the global variables
plat_nodes = None
plat_col_units = None
plat_operators = None

#This section collects responses from the user to calculate the IMC Base Platform Requirements

def gather_plat_req():
        global plat_nodes, plat_col_units, plat_operators
        plat_nodes = 0
        plat_col_units = 0
        plat_operators = 0
        plat_operators = input('What is the expected number of concurrent online operators?: ')
        single_dev = input('Do you want to manage single devices? Y/N: ')
        if single_dev == "Y" or single_dev == "y":
            SingleDevices()
        server_dev = input('Do you want to manage Servers? Y/N: ')
        if server_dev == "Y" or server_dev == "y":
            ServerDevices()
        stack_dev = input("Do you want to manage stacks of switches? Y/N: ")
        if stack_dev == "Y" or stack_dev == "y":
            StackDevices()
        print('Total nodes is : ' + str(plat_nodes))
        print ("Total collection units is: "+ str(plat_col_units))
        print("Total concurrent operators is " +str(plat_operators))
        Plat_HW_Guidance()

def StackDevices():
       global plat_nodes, plat_col_units
       stack_count = int(input("What is the total number of network Stacks you want to monitor:"))
       stack_devices= int(input("Average number of switches in a stack:"))
       number_of_interfaces = int(input("Average number of interfaces you want to monitor per device:"))
       number_of_monitors = int(input("Number of Metrics you want to monitor per interface:"))
       cpu = int(1*stack_devices) 
       memory = int(1*stack_devices)
       reachability = int(1)
       response_time = int(1)
       total_instances = int( (number_of_interfaces * number_of_monitors ) + cpu + memory +reachability + response_time)
       polled_units = int(stack_count*total_instances)
       poll_interval = int(input("How many minutes should we wait between polling a device: (minutes)"))
       stack_units = int(polled_units*(5/poll_interval))
       plat_col_units = ( plat_col_units + stack_units )
       plat_nodes = (plat_nodes + stack_count)
       return plat_col_units, plat_nodes

def ServerDevices():
       global plat_nodes, plat_col_units
       server_devices = int(input("What is the total Number of Servers you want to monitor:"))
       proc_quantity = int(input("Average number of processors in a server:"))
       cores_quantity = int(input("Average number of cores per processor:"))
       num_drives = int(input("Average number of logical drives per server:"))
       number_of_interfaces = int(input("Average number of interfaces you want to monitor per server:"))
       number_of_monitors = int(input("Number of Metrics you want to monitor per interface:"))
       cpu = (1*(proc_quantity*cores_quantity))
       memory = (1)
       reachability = (1)
       response_time = (1)
       total_instances = int( (number_of_interfaces  ) + cpu + memory +reachability + response_time+num_drives)
       polled_units = int(server_devices*total_instances)
       poll_interval = int(input("How many minutes should we wait between device poll in minutes:"))
       server_col_units =  int(polled_units*(5/poll_interval))
       plat_col_units = ( plat_col_units + server_col_units )
       plat_nodes = (plat_nodes + server_devices)
       return plat_col_units, plat_nodes
                

def SingleDevices():
       global plat_nodes, plat_col_units
       single_devices=int(input('''What is the total number of network devices you wish to monitor\nThis includes routers, wireless controllers, and non-stacked switches: '''))
       number_of_interfaces = int(input("Average number of interfaces you want to monitor per device:"))
       number_of_monitors = int(input("Number of Metrics you want to monitor per interface:"))
       cpu = (1)
       memory = (1)
       reachability = (1)
       response_time = (1)
       total_instances = int( (number_of_interfaces * number_of_monitors ) + cpu + memory +reachability + response_time)
       polled_units = int(single_devices*total_instances)
       poll_interval = int(input("How many minutes should we wait between device poll in minutes"))
       single_dev_units = (polled_units*(5/poll_interval))
       plat_col_units = ( plat_col_units + single_dev_units )
       plat_nodes = (plat_nodes + single_devices)
       return plat_col_units, plat_nodes

#This section will import the HPIMCHardwareSchemes.csv file as list of dictionaries and compare the values collected above to provide hardware platform recommendations

def Plat_HW_Guidance(plat_col_units=plat_col_units, plat_nodes=plat_nodes, plat_operators=plat_operators):
            #import csv file as dictionary
            with open ('HPIMC_Plat_HardwareSchemes.csv') as csvfile:
                       reader = csv.DictReader(csvfile)
                       for i in reader:
                           if i['Module'] == 'PLAT' and int(plat_operators) <= int(i['Max. online operators']) and int(plat_nodes) <= int(i['Node count']) and int(plat_col_units)  <= int(i['Collection units']):
                               print (json.dumps(i, indent=4))
                               break

#Defines the program to be run
        
def main():            
    imc_plat = input("Is this a new install Y/N:")
    if imc_plat == "Y" or imc_plat == "y":
        gather_plat_req()

    
    


if __name__ == "__main__":
    main()
