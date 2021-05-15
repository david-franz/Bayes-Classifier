# we start at 1 so we don't get any features with count 0
# ith index of list is the ith word of our list of spam words:
# 		• index 0 of that list is the count of emails that DON'T have that word (false)
# 		• index 1 of that list is the count of emails that DO have that word (true)
not_spam_counts = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]
spam_counts = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]

class DataLoader:

	@staticmethod
	def load_data_as_counts():
		with open("spamLabelled.dat") as f: # this will automatically close the file f when we exit this block
			lines = ["".join(line.split()) for line in f.readlines()]

			for line in lines:
				line_is_spam = bool(int(line[len(line)-1]))

				if line_is_spam:
					# character will be 0 or 1 to indicate whether that word is in the email
					for index, character in enumerate(line[:-1]):
						spam_counts[index][int(character)] += 1

				else: # this means that the document has been classified as not spam
					# character will be 0 or 1 to indicate whether that word is in the email
					for index, character in enumerate(line[:-1]):
						not_spam_counts[index][int(character)] += 1

				

		# we return a tuple of the lists described above with:
		# 		• index 0 is the list of counts where the email ISN'T marked as spam (false)
		# 		• index 1 is the list of counts where the email IS marked as spam (true)
		return not_spam_counts, spam_counts