from __future__ import division
import random

sets = {}
total = 0
same = 0


def odds_are():
	total = 0
	same = 0
	for i in xrange(100000):
		random_number_one = random.randint(1, 10)
		random_number_two = random.randint(1, 10)
		key = (random_number_one, random_number_two)
		sets[key] = sets.get(key, 0) + 1

	for item in sets.items():
		print str(item[0]) + ": " + str(item[1])
		total += int(item[1])
		if (item[0][0] == item[0][1]):
			same += int(item[1])
	print "{:.0%}".format(same / total)

odds_are()