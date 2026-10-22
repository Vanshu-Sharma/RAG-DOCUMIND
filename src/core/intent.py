
import re

GREETINGS = {
    "hi", "hii", "hiii", "hello", "hey",
    "good morning", "good afternoon", "good evening",
    "how are you", "thanks", "thank you", "bye", "goodbye",
}


def is_greeting(message: str) -> bool:
    text = re.sub(r"[^\w\s]", "", message.lower()).strip()
    return text in GREETINGS
