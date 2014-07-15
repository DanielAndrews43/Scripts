total_words = 0
total_letters = 0
letters = {}
for word in open("/usr/share/dict/words"):
	total_words += 1
	total_letters += len(word)
	letters[len(word)] = letters.get(len(word), 0) + 1

print "There are {0} words averaging {1} letters each".format(total_words, (total_letters/total_words))
print
for key, value in letters.items():
	print str(key) + ":\t" + str(value)