'''
Topic   : Arrays
Problem : Gas Station
Link    : https://leetcode.com/problems/gas-station/
'''
def canCompleteCircuit(gas, cost):
    start_index, net_gas, tank = 0,0,0
    
    for i, gas_amount in enumerate(gas):
        tank += gas_amount- cost[i]
        net_gas += gas_amount - cost[i]
        if tank < 0:
            start_index = i+1
            tank = 0
    
    return -1 if net_gas < 0 else start_index