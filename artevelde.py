# Recursive calculation to check if a sum of a set of numbers matches a target amount
# Author: some dude on teh internetz
# Adapted for PBE's bekistingshout by Freduardo <freduardo@gmail.com>
# Written in python

def subset_sum_recursive(numbers,target,partial):
    s = sum(partial)

    #check if the target number exists in the range
    if s == target: 
        print "sum(%s)=%s"%(partial,target)
    if s >= target:
        return # if so easy-peasy!

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum_recursive(remaining,target,partial + [n]) 

def subset_sum(numbers,target):
    #intermediate function to start the recursion.
    #the recursion start with an empty list as partial solution.
    subset_sum_recursive(numbers,target,list())

if __name__ == "__main__":
    subset_sum([11228.59,12108.49,6242.37,2328.72,3469.5,3469.5,2759.96,2004.8,1718.4,1718.4,2291.2,3245.25,2097.9,471.5,337.5,419.53],51557.4)    
    
    #Outputs:    
    #sum([3, 8, 4])=15    
    #sum([3, 5, 7])=15    
    #sum([8, 7])=15    
    #sum([5, 10])=15
