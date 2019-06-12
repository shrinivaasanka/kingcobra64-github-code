/***************************************************************************************
#NEURONRAIN KINGCOBRA  - Kernelspace Messaging
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.
#-----------------------------------------------------------------------------------------
#Copyleft (Copyright+):
#Srinivasan Kannan (alias) Ka.Shrinivaasan (alias) Shrinivas Kannan
#Ph: 9791499106, 9003082186
#Krishna iResearch Open Source Products Profiles:
#http://sourceforge.net/users/ka_shrinivaasan,
#https://github.com/shrinivaasanka,
#https://www.openhub.net/accounts/ka_shrinivaasan
#Personal website(research): https://sites.google.com/site/kuja27/
#emails: ka.shrinivaasan@gmail.com, shrinivas.kannan@gmail.com,
#kashrinivaasan@live.com
#-----------------------------------------------------------------------------------------
*****************************************************************************************/

#include <stdio.h>
#include <unistd.h>

int enable_cloud_perfect_forwarding=1;

void KingCobra_ServiceRequest(void* args)
{
 	printf("KingCobra_ServiceRequest invoked\n");	
	if(enable_cloud_perfect_forwarding)
	{
		printf("KingCobra - Cloud Perfect Forwarding C++ std::move client-server binaries invoked\n");
		execl("/bin/sh", "sh", "-c", "/media/shrinivaasanka/0fc4d8a2-1c74-42b8-8099-9ef78d8c8ea2/home/kashrinivaasan/linux-4.1.5/drivers/kcobra/kingcobra_cloud_perfect_forwarding.sh", (char *) 0);
	}
}
