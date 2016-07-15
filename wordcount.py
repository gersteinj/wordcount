import logging
import string

document = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""

cleanedText = " "

logging.basicConfig(level = logging.DEBUG)
logger = logging.getLogger(__name__)

logger.info("Reading document now")

# Read each character in the text
for char in document:
    # logger.debug(char)

    # TODO: Check to see if the character is alphanumeric 
    alphanumeric = char in string.ascii_letters or char in string.digits
    logger.debug("alphanumeric status of %s: %s" % (char, alphanumeric))
    # TODO: If character is alphanumeric, leave it alone
    if not alphanumeric:
    	if char == " ":
    		logger.debug("But it is a space")
    # TODO: If character isn't alphanumeric and is space, leave it alone

    # TODO: If character isn't alphanumeric and isn't space, remove it