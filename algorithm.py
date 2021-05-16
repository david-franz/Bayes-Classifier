# determines whether or not an email is spam based on whether or not the email contains certain words
# classification: either spam or not spam

from dataloader import DataLoader

# not_spam_counts (classified_as_spam = false) at index 0 of tuple, spam_counts (classified_as_spam = true) at index 1
word_counts__classified_as_spam = (not_spam_counts, spam_counts, probability_of_spam) = DataLoader.load_data_as_counts("spamLabelled.dat")

# # # # # # # # # # # # # #	#
#	Probability Functions	#
# # # # # # # # # # # # # #	#
def probability_of_spam():
	return word_counts__classified_as_spam[-1]

def probability_of_not_spam():
	return 1 - probability_of_spam()

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


# # # # # # # # # # # # #
#	Baye's Classifier	#
# # # # # # # # # # # # #
def bayes_classifier(filename):
	# we get a list binary representation corresponding to the word content of each email in our unlablled data
	emails_info = DataLoader.load_data_as_binary_strings(filename)

	probabilities_of_words = list()

	for email_info in emails_info:
		# these will multiply with the probability calculations below and make no difference on them
		probability_email_is_spam = 1.0
		probability_email_is_not_spam = 1.0

		for index, character in enumerate(email_info):
			if bool(int(character)): # this means that the emails contains number index
				probability_email_is_spam *= posterior_probability_of_word_given_class(index, True)
				probability_email_is_not_spam *= posterior_probability_of_word_given_class(index, False)
			else:
				probability_email_is_spam *= posterior_probability_of_not_word_given_class(index, True)
				probability_email_is_not_spam *= posterior_probability_of_not_word_given_class(index, False)

		probability_email_is_spam *= probability_of_spam() 
		probability_email_is_not_spam *= probability_of_not_spam()

		probabilities_of_words.append((probability_email_is_not_spam, probability_email_is_spam))

	return probabilities_of_words


if __name__ == "__main__":
	print('''From our training set, we have:\n
• The counts of the 12 words for emails classified as spam:\n
{}\n\n

• And the counts of the 12 words for emails classified as not spam:\n
{}\n\n'''
	.
	format(spam_counts, not_spam_counts))

	print("Probabilities of words given class label:")
	for class_label in range(2):
		for index in range(12):
			print("P(word_{} is present | class label is {}) = {}"
				.format(index+1, "\'spam\'" if bool(class_label) else "\'not spam\'", posterior_probability_of_word_given_class(index, bool(class_label))))

	probabilities_of_words = bayes_classifier("spamUnlabelled.dat")

	print("\n-------------------------------------")
	print("Results on Unlabelled Data:")
	print("-------------------------------------")

	for index, probability_of_word in enumerate(probabilities_of_words):
		probability_email_is_not_spam = probability_of_word[0]
		probability_email_is_spam = probability_of_word[1]

		print("-------------------------------------")

		if probability_email_is_not_spam <= probability_email_is_spam: # think about which inequality I want to use here
			print("email number {} classified as spam".format(index+1))
		else:
			print("email number {} classified as not spam".format(index))

	print("-------------------------------------\n")