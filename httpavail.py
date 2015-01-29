import sys, requests, argparse
from retrying import retry

argparser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
argparser.add_argument('url')
argparser.add_argument('-t', '--timeout', type=int, default=120, help='total timeout in seconds to wait for the url to be available')
argparser.add_argument('-d', '--delay', type=int, default=1, help='delay in seconds between each retry')
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
