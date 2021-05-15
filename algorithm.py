# determines whether or not an email is spam based on whether or not the email contains certain words
# classification: either spam or not spam

import math

from dataloader import DataLoader

word_counts__classified_as_spam = (not_spam_counts, spam_counts) = DataLoader.load_data_as_counts() # spam_counts (true) at index 1, not_spam_counts (false) at index 0

# probably need another calculate probability (not a conditional one)

# class meaning classified as spam or not
def probability_of_index_given_class(index_of_count, classified_as_spam):
	assert type(classified_as_spam) is bool

	return (word_counts__classified_as_spam[classified_as_spam][index_of_count] / 
	(word_counts__classified_as_spam[True][index_of_count] + 
		word_counts__classified_as_spam[False][index_of_count]))


if __name__ == "__main__":
	print('''In our training set, we have:\n
	The counts of the 12 words for emails classified as spam:\n

	\t{}\n\n

	And the counts of the 12 words for emails classified as not spam:\n

	\t{}\n\n'''
	.
	format(spam_counts, not_spam_counts))

	print(word_counts__classified_as_spam[True])
	print(word_counts__classified_as_spam[False])

	#print(probability_of_index_given_class(0, True))
	#print(probability_of_index_given_class(2, True))
	#print(probability_of_index_given_class(7, False))
	#print(probability_of_index_given_class(11, False))