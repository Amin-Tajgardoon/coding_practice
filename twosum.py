# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 19:00:03 2017

@author: Amin
"""

import numpy as np


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    output: list of two index that sums to target
    """
    dic = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if (complement in dic.keys()) and (dic[complement] != i):
            return [i, dic[complement]] 
        dic[nums[i]] = i


if __name__ == "__main__":
        
    nums = np.random.randint(0,1000000, size=500000).tolist()
    
    nums[len(nums)-2] = -1
    nums[len(nums)-1] = -1
    
    result = twoSum(nums, -2)
    assert result == [499999, 499998]      