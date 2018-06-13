A simple utility to help test AWS Lambda functions for SQL Injection vulnerabilities, using a local HTTP proxy, which transforms the SQLMap HTTP-based attacks to AWS Lambda invoke calls.

Run lambda-proxy
```console
$ python3 main.py
```
Update request.txt, which is the file containing your Lambda function's event data, and run

```console
$ sqlmap -r request.txt
```
