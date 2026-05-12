SECURITY DOCUMENTATION

**Policy Lifecycle Manager**

**1. Prompt Injection**

**Attackers may try to manipulate AI prompts.**

**Mitigation:**

**- Input sanitisation**

**- Prompt filtering**

**- Reject unsafe requests**



**2. SQL Injection**

**Attackers may send malicious SQL queries.**

**Mitigation:**

**- Input validation**

**- Parameterized queries**

**- ORM/JPA protection**



**3. Cross-Site Scripting (XSS)**

**Attackers may inject JavaScript into forms.**

**Mitigation:**

**- Remove script tags**

**- Escape frontend output**

**- Validate inputs**



**4. Broken Authentication**

**Unauthorised users may access protected APIs.**

**Mitigation:**

**- JWT authentication**

**- Token validation**

**- Protected routes**



**5. Rate Limit Abuse**

**Attackers may overload APIs with repeated requests.**

**Mitigation:**

**- flask-limiter**

**- Request throttling**

**- HTTP 429 responses**



**Day 1 Status**

**- Folder structure created**

**- SECURITY documentation completed**

