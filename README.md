# docker-httpavail

HTTP availability checker as a docker image. Performs a HTTP GET request against the given
URL and retries until either the expected HTTP status code (default: 200) is returned or
the timeout (default: 120s) is reached.

The exit code is 0 on success or 1 on timeout.


## Example

```
docker run --rm httpavail https://url-to-check.com:8080/path
```


## Usage

```
docker run --rm httpavail [-h] [-t TIMEOUT] [-d DELAY] [-s STATUS_CODE] url

positional arguments:
  url                   the URL to check

optional arguments:
  -h, --help            show this help message and exit
  -t TIMEOUT, --timeout TIMEOUT
                        total timeout in seconds to wait for the url to be
                        available (default: 120)
  -d DELAY, --delay DELAY
                        delay in seconds between each retry (default: 1)
  -s STATUS_CODE, --status-code STATUS_CODE
                        expected HTTP status code (default: 200)
```
