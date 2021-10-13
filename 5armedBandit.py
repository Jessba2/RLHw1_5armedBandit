#5armedBandit.py
#Jessica Barnett   RL hw1   10/11/2021

import numpy
from numpy import random

print("This program learns to pull the best lever!")
random.seed()

def bandit(leverNum):
    reward = random.normal(loc=meanMatrix[leverNum], scale=1, size=None)
    return reward

outerLoop=0
sumOf200rewardSums = 0
while (outerLoop <= 199):
    outerLoop = outerLoop + 1
    counter=0
    rewardSum=0
    #set meanMatrix for levers
    meanMatrix = numpy.random.randint(-5,5,size=5)

    #Initialize, for a=1 to 5, Q(a) = 0 and N(a)=0
    NumTimesMatrix = [0, 0, 0, 0, 0]
    QValueMatrix = [0, 0, 0, 0, 0]
    while (counter<=99):
        counter = counter + 1
        epsilon = .4
        randomDec = random.random()
        if randomDec >= epsilon:
            A = numpy.argmax(QValueMatrix)
        else:
            A = random.randint(0, 5)
        reward = bandit(A)
        rewardSum = rewardSum + reward
        NumTimesMatrix[A] = 1 + NumTimesMatrix[A]
        newValue = QValueMatrix[A] + ((1/NumTimesMatrix[A])*(reward-QValueMatrix[A]))
        QValueMatrix[A] = newValue
    sumOf200rewardSums = sumOf200rewardSums + rewardSum
print("With epsilon value ", epsilon)
print("the average reward is ", sumOf200rewardSums/20000)