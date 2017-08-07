from pylab import *

N = 10  # Number of generations
S = 50  # Amount of seeds per plant
w1 = 0.1 # Fraction that survives winter
g1 = 0.4 # Fraction that germinates after winter
g2 = 0.2 # Two year surviving seed germination rate
P = int(input("Number of starting plants "))
K = S*w1*g1
K2 = S*w1*w1*(1-g1)*g2

oneyearplants = zeros(N)
twoyearplants = zeros(N)

generations = arange(N)

oneyearplants[0] = P
twoyearplants[0] = P
twoyearplants[1] = K*P
for n in range(2,N):
    twoyearplants[n] = K*twoyearplants[n-1]+K2*twoyearplants[n-2]
for n in range(1,N):
    oneyearplants[n] = K * oneyearplants[n-1]

#print (twoyearplants)
plot(generations, twoyearplants, 'g-', label="Two year seeds")
plot(generations, oneyearplants, 'r-', label="One year seeds")
xlabel('Generations in years')
ylabel('Number of plants')
title("Simulated plant growth")
legend(loc='upper left')
show()
