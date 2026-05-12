import re

HTML_TAG_PATTERN = re.compile(r"<[^>]*>")

PROMPT_INJECTION_PATTERNS = [
    "ignore previous instructions",
    "ignore all instructions",
    "forget previous instructions",
    "disregard previous instructions",
    "reveal system prompt",
    "show system prompt",
    "developer mode",
    "jailbreak",
    "bypass security",
    "override instructions"
]


def strip_html(text):
    return HTML_TAG_PATTERN.sub("", text)


def has_prompt_injection(text):
    text_lower = text.lower()

    for pattern in PROMPT_INJECTION_PATTERNS:
        if pattern in text_lower:
            return True

    return False


def sanitize_input(text):
    cleaned_text = strip_html(text).strip()

    if has_prompt_injection(cleaned_text):
        return {
            "safe": False,
            "cleaned_text": cleaned_text,
            "error": "Prompt injection detected. Request blocked."
        }

    return {
        "safe": True,
        "cleaned_text": cleaned_text,
        "error": None
    }