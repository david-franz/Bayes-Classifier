# determines whether or not an email is spam based on whether or not the email contains certain words
# classification: either spam or not spam

from dataloader import DataLoader

spam_counts, not_spam_counts = DataLoader.load_data_as_counts()

print('''In our training set, we have:\n
The count of the 12 words for emails classified as spam:\n

\t{}\n\n

And the count for the of the 12 words for emails classified as not spam:\n

\t{}\n\n'''
.
format(spam_counts, not_spam_counts))


