import sys, requests, argparse
from retrying import retry

argparser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
argparser.add_argument('url')
argparser.add_argument('-t', '--timeout', type=int, default=120, help='total timeout in seconds to wait for the url to be available')
argparser.add_argument('-d', '--delay', type=int, default=1, help='delay in seconds between each retry')
argparser.add_argument('-s', '--status-code', type=int, default=200, help='expected HTTP status code')
args = argparser.parse_args()


@retry(stop_max_delay = args.timeout * 1000, wait_fixed = args.delay * 1000)
def check():
    print('Checking', args.url, 'for HTTP code', args.status_code)
    sys.stdout.flush()

    response = requests.get(args.url, timeout = 1)
    if response.status_code != args.status_code:
        raise Exception('Unexpected HTTP status code {} (Wanted: {})'.format(response.status_code , args.status_code))


try:
    check()
    sys.exit(0)
except Exception as e:
    print(str(e))
    sys.exit(1)
