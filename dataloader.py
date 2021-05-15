# we start at 1 so we don't get any features with count 0
spam_counts = [1] * 12
not_spam_counts = [1] * 12

class DataLoader:

	@staticmethod
	def load_data_as_counts():
		with open("spamLabelled.dat") as f: # this will automatically close the file f when we exit this block
			f = open("spamLabelled.dat")

			lines = ["".join(line.split()) for line in f.readlines()]

			for line in lines:
				if bool(int(line[len(line)-1])): # this means that the document is classed as spam
					for i, c in enumerate(line[:-1]):
						if bool(int(c)):
							spam_counts[i] += 1

				else: # this means that the document has been classified as not spam
					for i, c in enumerate(line[:-1]):
						if bool(int(c)):
							not_spam_counts[i] += 1

		return spam_counts, not_spam_counts