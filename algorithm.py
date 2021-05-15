# determines whether or not an email is spam based on whether or not the email contains certain words
# classification: either spam or not spam

import math

from dataloader import DataLoader

# not_spam_counts (classified_as_spam = false) at index 0 of tuple, spam_counts (classified_as_spam = true) at index 1
word_counts__classified_as_spam =
	(not_spam_counts, spam_counts, probability_of_spam) = 
		DataLoader.load_data_as_counts()

def probability_of_spam():
	return word_counts__classified_as_spam[-1]

def probability_of_not_spam():
	return 1 - probability_of_spam()

def prior_probability_of_word(index_of_word):
	return ((word_counts__classified_as_spam[False][index_of_word][1] +
			 word_counts__classified_as_spam[True][index_of_word][1]) /
	   			(word_counts__classified_as_spam[False][index_of_word][0] +
			 	  word_counts__classified_as_spam[True][index_of_word][0] + 
			     word_counts__classified_as_spam[False][index_of_word][1] + 
				  word_counts__classified_as_spam[True][index_of_word][1]))

def prior_probability_of_not_word(index_of_word):
	return 1 - prior_probability_of_word(index_of_word)

# this returns the probability that an email contains a certain word for a given email class
# class meaning classified as spam (true) or not (false)
def posterior_probability_of_word_given_class(index_of_word, classified_as_spam): # posterior probability (given class)
	assert type(classified_as_spam) is bool

	return (word_counts__classified_as_spam[int(classified_as_spam)][index_of_word][1] / 
				(word_counts__classified_as_spam[int(classified_as_spam)][index_of_word][0] + 
				 word_counts__classified_as_spam[int(classified_as_spam)][index_of_word][1]))

# this returns the probability that an email doesn't contain a certain word for a given email class
def posterior_probability_of_not_word_given_class(index_of_word, classified_as_spam): # posterior probability (given class
	return 1 - posterior_probability_of_word_given_class(index_of_word, classified_as_spam)

if __name__ == "__main__":
	print('''From our training set, we have:\n
	• The counts of the 12 words for emails classified as spam:\n
	{}\n\n

	• And the counts of the 12 words for emails classified as not spam:\n
	{}\n\n'''
	.
	format(spam_counts, not_spam_counts))

	print(word_counts__classified_as_spam[True])
	print(word_counts__classified_as_spam[False])

	print(posterior_probability_of_word_given_class(0, True))
	print(posterior_probability_of_not_word_given_class(0, True))

	print(prior_probability_of_word(0))
	print(prior_probability_of_not_word(0))

	