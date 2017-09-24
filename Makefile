#
#Makefile for VIRGO queue 
#

ccflags-y := -w -I/media/ka_shrinivaasan/cbddc062-a016-4828-8780-21bc64cef1e8/linux-4.13.3/lib -I/media/ka_shrinivaasan/cbddc062-a016-4828-8780-21bc64cef1e8/linux-4.13.3/include -I/media/ka_shrinivaasan/cbddc062-a016-4828-8780-21bc64cef1e8/linux-4.13.3/include/uapi/linux -DDEBUG

kingcobra_main_kernelspace_driver-y	+= kingcobra_main_kernelspace.o
obj-m               += kingcobra_main_kernelspace.o
