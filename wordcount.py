import logging
import string

document = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""

cleaned_text = ""

logging.basicConfig(level = logging.DEBUG)
logger = logging.getLogger(__name__)

logger.info("Reading document now")

# Read each character in the text
for char in document:
    # logger.debug(char)

    # Check to see if the character is alphanumeric; if so, add to cleaned_text 
    if char in string.ascii_letters or char in string.digits:
        logger.debug("%s is alphanumeric" % char)
        cleaned_text += char

    # If character isn't alphanumeric and is space, add to cleaned_text
    elif char == " ":
        logger.debug("But it is a space")
        cleaned_text += char
    # If character isn't alphanumeric and isn't space, don't add to cleaned_text
    # TODO: add abilitiy to check for contractions
    else:
        logger.debug("KILL IT!")

logger.info("Your new text is: %s" % cleaned_text)

words = cleaned_text.split(" ")

print(words)
