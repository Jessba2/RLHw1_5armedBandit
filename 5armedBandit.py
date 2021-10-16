#5armedBandit.py
#Jessica Barnett   RL hw1   10/11/2021

import numpy
from numpy import random
import matplotlib.pyplot as plt

print("This program learns to pull the best lever!")
random.seed()

def bandit(leverNum):
    reward = random.normal(loc=meanMatrix[leverNum], scale=1, size=None)
    return reward

rewardMatrixPt4 = numpy.zeros((1000, 2000))
rewardMatrixPt1 = numpy.zeros((1000, 2000))
rewardMatrix0 = numpy.zeros((1000, 2000))
epsilonMatrix = [0, 0.02, 0.4]
differentEpsilonValues = 0
while(differentEpsilonValues <= 2):
    trial=0
    sumOf200rewardSums = 0
    while (trial <= 1999):
        timestep=0
        rewardSum=0
        #set meanMatrix for levers
        meanMatrix = numpy.random.randint(-5,5,size=5)

        #Initialize, for a=1 to 5, Q(a) = 0 and N(a)=0
        NumTimesMatrix = [0, 0, 0, 0, 0]
        QValueMatrix = [0, 0, 0, 0, 0]
        while (timestep <= 999):
            epsilon = epsilonMatrix[differentEpsilonValues]
            randomDec = random.random()
            if randomDec >= epsilon:
                A = numpy.argmax(QValueMatrix)
            else:
                A = random.randint(0, 5)
            reward = bandit(A)
            if (epsilon == 0):
                rewardMatrix0[timestep][trial] = reward
            elif (epsilon == .4):
                rewardMatrixPt4[timestep][trial] = reward
            elif (epsilon == .02):
                rewardMatrixPt1[timestep][trial] = reward
            else:
                print("ut oh")
            NumTimesMatrix[A] = 1 + NumTimesMatrix[A]
            newValue = QValueMatrix[A] + ((1/NumTimesMatrix[A])*(reward-QValueMatrix[A]))
            QValueMatrix[A] = newValue
            timestep = timestep + 1
        sumOf200rewardSums = sumOf200rewardSums + rewardSum
        trial = trial + 1
    differentEpsilonValues = differentEpsilonValues + 1

averagesMatrixPt4 = numpy.mean(rewardMatrixPt4, axis=1)
averagesMatrixPt1 = numpy.mean(rewardMatrixPt1, axis=1)
averagesMatrix0 = numpy.mean(rewardMatrix0, axis=1)
v=averagesMatrixPt4
z=averagesMatrixPt1
w=averagesMatrix0
x=numpy.arange(0, 1000)
#print("With epsilon value ", epsilon)
#print("the average reward is ", sumOf200rewardSums/20000)
plt.title("Average Reward by Timestep")
plt.xlabel("Steps")
plt.ylabel("Average Reward")
plt.plot(x, w, "red", label = '0 (greedy)')
plt.plot(x, z, "blue", label = '0.02')
plt.plot(x, v, "green", label = '0.4')
plt.legend(title='Epsilon value')
plt.show()
