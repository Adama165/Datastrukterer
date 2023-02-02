import max_subsequence
import random
import time
import matplotlib.pyplot as plt

testList = []
timePrior = 0
timeDuration = 0
results = []
listLengths = []

def TimeInFunctionCall(fun, listLength):
    testList = random.sample(range(-1000000,1000000),listLength)
    print(testList)
    timePrior = time.process_time()
    funoutput = fun(testList)
    print(funoutput)
    timeDuration = time.process_time() - timePrior
    return timeDuration

def timeInFunctionCalls(fun, listLengths):
    results = []
    for i in listLengths:
        results.append(TimeInFunctionCall(fun, i))
    return results

userInput = input("What function? max1/max2/max3 ")
if userInput == "max1":
    fun = max_subsequence.max_subsequence1
if userInput == "max2":
    fun = max_subsequence.max_subsequence2
if userInput == "max3":
    fun = max_subsequence.max_subsequence3
else:
    "nope"

while len(listLengths) != 5:
    listLength = int(input("How long shall the list be? "))
    listLengths.append(listLength)
    print(listLengths)

results = timeInFunctionCalls(fun, listLengths)
print(listLengths)
print(results)

plt.plot(listLengths, results)
plt.xlabel("List length")
plt.ylabel("time(s)")
plt.title("Measurement for time")
plt.show()