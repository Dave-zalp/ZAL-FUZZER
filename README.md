![logo](Images/banner.png)

##                     ZAL-FUZZER
<hr>

### ZAL-FUZZER is a python based web fuzzer designed to help web pentesters automate the discovery of endpoints / paths contained in a web application.

## USAGE

```bash
git clone https://github.com/Dave-zalp/ZAL-FUZZER.git
pip install requirements.txt
python main.py -u https://google.com -w secret/fuzz.txt -mc 200 -th 10
```

# Required Tasks

## Features to Implement

- [ ] Can Headers, Cookies and Proxies to Request
- [ ] Can specify RandomUserAgent
- [ ] Can Follow 302 Redirections
- [ ] Don't Bind the url with wordlist before fuzzing
- [x] Request logs matchCodes and logs all codes if match isn't specified.

