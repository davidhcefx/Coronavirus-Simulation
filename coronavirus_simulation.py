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
histogram = []

for d in range(days):
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

	count = 0
	for i, _ in enumerate(people):
		if people[i] > 0:
			count += 1
	histogram.append(count)
	print('Day', d, ':', count, 'infected.')


plot.plot([i + 1 for i in range(days)], histogram,
		label='E*P = ' + str(exposure * prob))
plot.legend()
plot.xlabel('Days')
plot.ylabel('Infected')
plot.savefig('Plot.png')
