import re

BLOCKED_PATTERNS = [
    r"<script.*?>.*?</script>",
    r"DROP TABLE",
    r"SELECT .* FROM",
    r"INSERT INTO",
    r"--",
    r";"
]

def is_malicious(text):
    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            return True
    return False