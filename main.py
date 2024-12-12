import logging

from socid_extractor import extract, mutate_url, parse, parse_cookies

def join_cookies(cookies: dict):
    return ' ;'.join(f'{k}={v}' for k, v in cookies.items())

def print_info(info):
    logging.info('Result\n' + '-' * 40)
    for key, value in info.items():
        print('%s: %s' % (key, value))

def get_site_response(url, cookies=None, headers={}):
    page, status = parse(url, cookies, headers=headers, timeout=10)
    if status != 200:
        logging.info('Answer code {}, something went wrong'.format(status))
    return page

def search_profile(arg_url: str) -> dict:
    reqs = [(arg_url, set())]
    mutations = mutate_url(arg_url)
    if mutations:
        reqs += list(mutations)

    headers = {}
    for req in reqs:
        url, add_headers = req

        cookies = {}
        cookies.update(parse_cookies(''))
        cookies_str = join_cookies(cookies)

        print(f'Analyzing URL {url}...')
        url_headers = dict(headers)
        url_headers.update(add_headers)

        page = get_site_response(url, cookies_str, url_headers)
        info = extract(page)
        if info:
            return info
    
    return {}