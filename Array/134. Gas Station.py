
# original Time Limit Exceeded
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

#       start = for n in ags:
        #         if n = len(-1): pass to first
    
#         if n = start -1:
            # break
    
        
        # base case
        if sum(gas) - sum(cost) < 0:
            return -1

        for i in range(len(gas)):

            tank = gas[i]
            index = i
            breke_index = i
            switch = 0
            if breke_index == -1:
                breke_index = len(gas)-1


        #             make sure not to -
            while index != len(gas):

                tank -= cost[index]

                if tank < 0:
                   break 

                if index == breke_index and switch == 1:
                    return i   


                if index == len(gas)-1:

                    index = 0
                    tank += gas[index]     
                    continue




                switch = 1
                index += 1
                tank += gas[index]   
            
        return -1
                
# https://leetcode.com/problems/gas-station/discuss/1276287/Simple-one-pass-python-solution

class Solution:
	def canCompleteCircuit(self, gas, cost):

        # base case
		if sum(gas) - sum(cost) < 0:
			return -1

		gas_tank = 0  # gas available in car till now
		start_index = 0  # Consider first gas station as starting point

		for i in range(len(gas)):

			gas_tank += gas[i] - cost[i]

			if gas_tank < 0:  # the car has deficit of petrol
			    start_index = i+1  # change the starting point
			    gas_tank = 0  # make the current gas to 0, as we will be starting again from next station

		return start_index
                
        
        


                

                
        
        


                

                
        
        

