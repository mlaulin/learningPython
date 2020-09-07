#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:18:47 2020

@author: mlaulin
"""


def create_student():
    student_name = input("Please enter the Student Name: ")
    science = float(input("Enter the marks for Science: "))
    math = float(input("Enter the marks for Math: "))
    sociology = float(input("Enter the marks for Sociology: "))
    language = float(input("Enter the marks for Language: "))
    music = float(input("Enter the marks for Music: "))

    student_total = science + math + sociology + language + music
    student_avg = student_total / 5

    student_data = {
        'Name': student_name,
        'Subject Scores': {
            'Science': science,
            'Math': math,
            'Sociology': sociology,
            'Language': language,
            'Music': music
        },
        'Total Score': student_total,
        'Average Marks': student_avg
    }

    return student_data


print(create_student())
