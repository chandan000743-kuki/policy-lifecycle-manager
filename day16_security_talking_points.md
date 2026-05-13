Day 16 - Security Talking Points

1. JWT Authentication
We implemented JWT-based access verification to prevent unauthorized access to protected endpoints. Requests without valid tokens return 401 Unauthorized or 403 Forbidden responses.

2. Rate Limiting
Rate limiting was added to block excessive repeated requests. After the allowed request threshold is exceeded, the API returns 429 Too Many Requests.

3. Input Sanitisation and XSS Protection
The AI service validates and sanitises incoming input to block malicious payloads such as XSS scripts and prompt injection attempts.

4. OWASP ZAP Security Testing
OWASP ZAP baseline and active scans were performed. Security headers were added using flask-talisman, and all Critical and High severity findings were resolved successfully.