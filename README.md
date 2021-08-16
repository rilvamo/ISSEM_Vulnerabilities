<h1>ISSEM_Vulnerabilities<h1>

<h2>#1 Brute Force Auth Tokens</h2>

Current auth token uses random function which can be determinisitic/predictable. This can be strengthened by using urandom function in Python.

<h2>#2 Same Token Generation</h2>
  
Currently when a token is created it is not validated if this token was created before. As we pointed out in the vulnerbaility #1, there is a issue with using random function and this might lead to compromise of the auth token. Hence when a token is created it needs to be validated if this token was created before.

<h2>#3 Cleartext data</h2>
  
Current client-server communication is in cleartext, this should be encrypted so that spoofed packet captures won't be any use.


<h2>#4 Denial of Service</h2>
 
Current setup allows unlimited socket connections for a sourceIP, this can be restricted by tracking number of connections by sourceIp and validating if it is more than the allowed connection limit.

  
