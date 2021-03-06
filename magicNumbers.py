#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:18:47 2020

@author: mlaulin
"""

magic_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]
group_1 = [1, 2, 3, 4, 5, 6, 7]  # initialize group 1
group_2 = [1, 2, 3, 4, 5, 6, 7]  # initialize group 2
group_3 = [1, 2, 3, 4, 5, 6, 7]  # initialize group 3

# Get length of the list to ensure you have 21 elements
# len_list = len(magic_list)
# print(len_list)

print("Pick a secret number from the list and remember: {} ".format(magic_list))

iteration_loop = 3
i = 0
choice = 0

input("Enter 0 to continue: ")

while i < iteration_loop:
    # print(i)

    g1c = 0  # initialize counter for group 1
    g2c = 1  # initialize counter for group 2
    g3c = 2  # initialize counter for group 3
    cnt = 0  # increment counter for appending group lists
     
    magic_loop = 7
    j = 0
    
    while j < magic_loop:
        
        grp1 = magic_list[g1c + cnt]
        grp2 = magic_list[g2c + cnt]
        grp3 = magic_list[g3c + cnt]
        
        group_1[j] = grp1
        group_2[j] = grp2
        group_3[j] = grp3
        
        cnt = cnt + 3
        j = j + 1
        
    print("Select the group in which you secret number is")
    print("Group 1: ", group_1)
    print("Group 2: ", group_2)
    print("Group 3: ", group_3)
    choice = input("Enter 1 for Group 1, 2 for Group 2 and 3 for Group 3: ")
    
    choice = int(choice)
    
    if choice == 1:
        magic_list = group_2 + group_1 + group_3
    if choice == 2:
        magic_list = group_3 + group_2 + group_1
    if choice == 3:
        magic_list = group_1 + group_3 + group_2
    
    # print(magic_list)  # Only for troubleshooting purposes
    
    i = i + 1
    
secret_num = magic_list[10]  # 11th position in the list
print("Your secret number is: {} ".format(secret_num))
