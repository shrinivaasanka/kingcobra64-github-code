# -------------------------------------------------------------------------------------------------------
# NEURONRAIN KingCobra - Module for Kernelspace Messaging and Computational Economics
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# --------------------------------------------------------------------------------------------------------
# K.Srinivasan
# NeuronRain Documentation and Licensing: http://neuronrain-documentation.readthedocs.io/en/latest/
# Personal website(research): https://acadpdrafts.readthedocs.io/en/latest/
# --------------------------------------------------------------------------------------------------------

class Neuro_EventNetGEM_HyperLedger(object):
	def __init__(self):
	    self.Neuro_HyperLedger_Vertices = open("Neuro_HyperLedger_EventNetGEMVertices.txt", "a")
	    self.Neuro_HyperLedger_Edges = open("Neuro_HyperLedger_EventNetGEMEdges.txt", "a")

	def algorithmic_trading(self,commodity, quantity, neuro_currency, buyer, seller, type):
	    verticestransaction = commodity + ":" + type + ":#" + neuro_currency + " - "
	    verticestransaction += buyer + "," + seller + " - "
	    verticestransaction += "(" + buyer + "," + seller + ")#\n" 
	    edgestransaction = "(" + buyer + "," + seller + ")\n" 
	    self.Neuro_HyperLedger_Vertices.write(verticestransaction)	
	    self.Neuro_HyperLedger_Edges.write(edgestransaction)	

if __name__=="__main__":
	neuro_hyperledger = Neuro_EventNetGEM_HyperLedger()
	neuro_hyperledger.algorithmic_trading("commodity1", "1000", "ff1f984d-ab18-4e69-9a3b-85ddd3c2cce7:1000000000000", "buyer1", "seller1","buy") 
	neuro_hyperledger.algorithmic_trading("commodity2", "2000", "ff1f984d-ab18-4e79-1a3b-85ddd3c6cde7:2000000000000", "buyer2", "seller2","buy") 
	neuro_hyperledger.algorithmic_trading("commodity3", "3000", "ff2f984d-ab18-5e79-1a3b-85ddd4c1cde7:3000000000000", "buyer3", "seller3","sell") 
	neuro_hyperledger.algorithmic_trading("commodity4", "8000", "ff2f994d-ab18-5e79-5a3b-85ddd4c3cde7:9000000000000", "buyer4", "seller4","sell") 
