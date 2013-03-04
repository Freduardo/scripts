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
    subset_sum([99.45,219.3,250.94,52.06,33.15,114.06,546.88,256.2,126.75,148.2,99.45,615.6,243.05,80.33,354.97,42.12,189,66.3,70.99,1986.93,46.8,12.1],3671.9)

    #Outputs:
    #sum([3, 8, 4])=15
    #sum([3, 5, 7])=15
    #sum([8, 7])=15
    #sum([5, 10])=15