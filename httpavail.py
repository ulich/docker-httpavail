import sys, requests, argparse
from retrying import retry

argparser = argparse.ArgumentParser()
argparser.add_argument('url')
argparser.add_argument('-t', '--timeout', type=int, default=120)
argparser.add_argument('-d', '--delay', type=int, default=1)
args = argparser.parse_args()


@retry(stop_max_delay = args.timeout * 1000, wait_fixed = args.delay * 1000)
def check():
    print('Checking', args.url)
    sys.stdout.flush()

    response = requests.get(args.url, timeout = 1)
    response.raise_for_status()
    return response.status_code

if check() == 200:
    sys.exit(0)
else:
    sys.exit(1)
