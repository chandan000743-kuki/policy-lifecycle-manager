Day 9 - PII Audit Report

Objective:
Verified that the AI service does not expose personal or sensitive information through prompts, logs, source code, or committed files.

Checks Performed

1. Secret/API Key Check

Command used:

Select-String -Path *.py,routes\*.py,services\*.py,middleware\*.py -Pattern "GROQ_API_KEY|api_key|password|secret|token"

Result:
No hardcoded API keys found
No passwords or secrets found in source code

2. Logging Check

Command used:

Select-String -Path *.py,routes\*.py,services\*.py,middleware\*.py -Pattern "print|logger|logging"

Result:
 No sensitive logs found
 No unsafe print statements found

.env Verification

Command used:

git ls-files .env

Result:
 No output returned
.env file is not committed to Git

Findings:
No personal data exposure found
No secrets found in source files
No sensitive logs detected

Status:
PASS