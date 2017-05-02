import urllib.request, urllib.parse, urllib.error
import ssl
import gitsecrets

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def urlopen(url):
    secrets = gitsecrets.secrets()

    parms = urllib.parse.urlencode(secrets)

    if url.find('?') > 0 :
        url = url + '&'
    else:
        url = url + '?'
    
    url = url + parms

    # print('Retrieving', url)
    req = urllib.request.Request(
        url,
        data=None,
        headers={'User-Agent': 'giturl.py from www.py4e.com/code3'
        }
    )
    connection = urllib.request.urlopen(req, context=ctx)
    str_json = connection.read().decode()
    headers = dict(connection.getheaders())
    return (str_json, headers)

