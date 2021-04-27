"""
Program to calculate and output mean and standard deviation of a set of 5 measurements

"""

import statistics
import math
import os

"""
Writes Dat file values into a list

Returns a list
"""
def writeDatFileToList(file_path):
    numbers = []
    if os.path.exists(file_path):
        with open(file_path) as SDnumbers_file:
            for line in SDnumbers_file:
                (key, val) = line.split()
                numbers.append(float(val))
        return numbers
    else:
        return "File doesn't exists, please ensure dat file is in the same folder as the script"

"""
Returns calculated mean value given a list of numbers
"""

def calculateMean(numbers):
    numTotal = 0.0
    if len(numbers) != 0:
        for number in numbers:
            numTotal = numTotal + number
        return round(numTotal/len(numbers), 3)
    else:
        return "Numbers list is empty"

"""
Returns calculated variance given a list of numbers
"""
def calculateVariance(numbers):
    squaredDifferences = []
    meanValue = calculateMean(numbers)
    for num in numbers:
        differencesSquared = (num-meanValue)**2
        squaredDifferences.append(differencesSquared)
    return sum(squaredDifferences)/(len(numbers)-1)

"""
Calculates Standard deviation given file path
to file containing float values

Returns a float value rounded to 4 decimal places
"""
def calculateStandardDeviation(file_path):
    numbers = writeDatFileToList(file_path)
    variance = calculateVariance(numbers)
    return round(math.sqrt(variance), 4)

"""
METHOD 2
Calculates Standard deviation from statistics module
using stdev() method

Returns a float value given the file path
"""
def standardDeviation(filepath):
    numbers = []
    if os.path.exists(filepath):
        with open(filepath) as SDnumbers_file:
            for line in SDnumbers_file:
                (key, val) = line.split()
                numbers.append(float(val))
            if len(numbers) == 0:
                return "invalid input"
            else:
                return round(statistics.stdev(numbers), 4)
    else:
        return "File doesn't exists, please ensure dat file is in the same folder as the script"
"""
Output results
"""

numbers = writeDatFileToList("SDnumbers.dat")
print('Mean: ',calculateMean(numbers))
print('Standard Deviation: ',calculateStandardDeviation("SDnumbers.dat"))
print('Method 2 Standard Deviation: ',standardDeviation("SDNumbers.dat"))

