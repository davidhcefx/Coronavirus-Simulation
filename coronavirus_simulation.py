import random
import matplotlib.pyplot as plot

# A program to simulate the spread of Coronavirus 2019.
# The prob and exposure is the key component affecting the curve.

n = 100000   # number of population
days = 30 * 6
prob = 0.024  # infection probability
exposure = 5  # number of others each person interactive with each day
effective_time = 10  # how long can a infected person infect others
initial = 10  # initial number of infections

# Assumption: Infected people will be immune to this virus.

people = [10] * initial + [0] * (n - initial)
newly_infected = []
total_infected = []

for d in range(days):
	newcases = 0
	# Decrease effective_time of each infected people
	for i, _ in enumerate(people):
		if people[i] == 1:
			people[i] = -1  # immunity
		elif people[i] > 0:
			people[i] -= 1

	for i, _ in enumerate(people):
		if people[i] > 0:
			# Infected people go to interact with exposure others
			for e in range(exposure):
				# Decide whether to infect this person or not
				if random.random() < prob:
					idx = random.randint(0, n - 1)
					if people[idx] == 0:
						people[idx] = effective_time
						newcases += 1

	total = 0
	for i, _ in enumerate(people):
		if people[i] != 0:
			total += 1
	newly_infected.append(newcases)
	total_infected.append(total)
	print('[Day %d] New cases: %d, Total: %d' % (d, newcases, total))


x = [i + 1 for i in range(days)]
plot.plot(x, newly_infected, label='Newly infected')
# plot.plot(x, total_infected, label='Total infected')
plot.legend()
plot.xlabel('Days')
plot.title('E*P = ' + str(exposure * prob))
plot.savefig('Plot.png')
