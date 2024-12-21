import random as rand
import numpy as np
import matplotlib.pyplot as plt
import collections as col


p = 2**31-1
N = p-1
n = 10**4
#k = 2
#c = 10
#m = c*n
#start = rand.randint(0,N-1-m)
a = np.array([],dtype = int)
b = np.array([],dtype = int)
seeds = np.array([],dtype = int)

a_temp = []
b_temp = []
seeds_temp = []




def chooseVals(k_inp,c_inp):
    global m, a, b, seeds, start, bloom1, bloom2,k,c
    k = k_inp
    c = c_inp
    m = c*n
    a = []
    b = []
    seeds = []
    a_temp = []
    b_temp = []
    seeds_temp = []
    start = rand.randint(0,N-1-m)
    for i in range(k):
        a_temp.append(rand.randint(1,p-1))
        b_temp.append(rand.randint(0,p-1))
        seeds_temp.append(rand.randint(0,100))
    a = np.concatenate((a, np.array(a_temp)))
    b = np.concatenate((b, np.array(b_temp)))
    #print("a",a)
    #print("b",b)
    seeds = np.concatenate((seeds, np.array(seeds_temp)))
    bloom1 = [0]*m
    bloom2 = [0]*m
    #print("k",k)
    

def h1(x):
    nums = []
    for i in range(k):
        #print("k in h1",k)
        nums.append(((a[i]*x+b[i])%p)%m)
    return np.array(nums, dtype=int)

def h2(x):
    nums = []
    #print("seeds",seeds)
    #print("k in h2",k)
    for seed in seeds:
        rand.seed(int(seed)+int(x))
        nums.append(rand.randint(0,m-1))
    return np.array(nums, dtype=int)

def add1(x):
    nums1 = h1(x)
    for num in nums1:
        bloom1[num]=1
def add2(x):
    nums2 = h2(x)
    for num in nums2:
        bloom2[num]=1

def contains1(x):
    nums1 = h1(x)
    for num in nums1:
        if bloom1[num]==0:
            return False
    return True

def contains2(x):
    nums2 = h2(x)
    for num in nums2:
        if bloom2[num]==0:
            return False
    return True

