# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from math import floor


def getFuelRec(Mass):
    return (floor(int(Mass)/3))-2

def part1():
    return map(getFuelRec, massList)
            
def part2():
    totalFuel = 0
    for fuel in indivFuel:
        while fuel > 0:
            totalFuel = totalFuel + fuel
            fuel = getFuelRec(fuel)
    return totalFuel

with open(("input.txt"), 'r') as txtFile:
    massList = txtFile.readlines();

indivFuel = part1()  
print("Day 1 Part 1: ", sum(indivFuel))
print("Day 1 Part 2: ", part2())