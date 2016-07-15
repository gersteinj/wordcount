import logging
import string

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

def clean(raw_string):
    """Takes in a string and returns a string with all non-alphanumeric and non-space characters stripped out"""
    cleaned_text = ""
    # Read each character in the text
    for char in raw_string:
        # Check to see if the character is alphanumeric or a space. If so, add to cleaned text
        if char in string.ascii_letters:
            logger.debug("%s is a letter" % char)
            cleaned_text += char
        elif char in string.digits:
            logger.debug("%s is a number" % char)
            cleaned_text += char
        elif char == ' ':
            logger.debug('space')
            cleaned_text += char
        else:
            logger.debug('Don\'t bother with that one')

    logger.info("Your result is: %s \n" % cleaned_text)

    return cleaned_text


def split_words(clean_string):
    """Takes a multi-word string and returns a list containing each word"""
    words = clean_string.split(" ")
    logger.info("Your words are: %s \n" % words)
    return words

def count_words(word_list):
    """Takes in a list of words and returns a dictionary of word counts"""
    word_count = {}
    for word in word_list:
        # If the word has already been added to the dictionary, increment it
        if word in word_count:
            logger.debug("%s is in word_count %s times" % (word, word_count[word]))
            word_count[word] += 1
            logger.debug("%s is in word_count %s times" % (word, word_count[word]))
        # Otherwise, add it with a count of 1
        else:
            logger.debug("%s wasn't in here yet." % word)
            word_count[word] = 1
            logger.debug("%s is in word_count %s times" % (word, word_count[word]))
    logger.info("Here are your word counts: %s \n" % word_count)
    return word_count


def wordcount(raw_string):
    return count_words(split_words(clean(raw_string)))


if __name__ == "__main__":
    document = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""
    counted_words = count_words(split_words(clean(document)))