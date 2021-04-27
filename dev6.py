import statistics
import math

"""
Writes Dat file values into a list

Returns a list
"""
def writeDatFileToList(filepath):
    numbers = []
    with open(filepath) as SDnumbers_file:
        for line in SDnumbers_file:        
            (key, val) = line.split()        
            numbers.append(float(val))
    return numbers

"""
Returns calculated mean value given a list of numbers
"""
def calculateMean(numbers):
    numTotal = 0.0
    for number in numbers:
        numTotal = numTotal + number    
    return round(numTotal/len(numbers), 3)

"""
Returns calculated Variance given a list of numbers
"""    
def calculateVariance(numbers):
    squaredDifferences = []
    meanValue = calculateMean(numbers)
    for num in numbers:
        differencesSquared = (num-meanValue)**2
        squaredDifferences.append(differencesSquared)
    return sum(squaredDifferences)/(len(numbers) -1)

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

Returns float value given the file path
"""
def standardDeviation(filepath):
    numbers = []
    with open(filepath) as SDnumbers_file:
        for line in SDnumbers_file:        
            (key, val) = line.split()        
            numbers.append(float(val))    
    return round(statistics.stdev(numbers), 4)




numbers = writeDatFileToList('SDNumbers.dat')
print('Mean: ',calculateMean(numbers))
print('Standard Deviation: ', calculateStandardDeviation('SDNumbers.dat'))
print('Standard Deviation: ', standardDeviation('SDNumbers.dat'))







