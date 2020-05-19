import urllib.request, urllib.parse, urllib.error
import json
import giturl

api_url = 'https://api.github.com'

repos = [
'users/csev',
'orgs/tsugiproject',
'orgs/tsugitools',
'orgs/tsugicloud'
]

pulls = dict()

for repo in repos:
    print('Checking repo:', repo)
    url = api_url + '/' + repo + '/repos' 

    # print('Retrieving', url)
    (str_json, headers) = giturl.urlopen(url)
    # print('Retrieved', len(str_json), 'characters')

    try:
        js = json.loads(str_json)
    except:
        print('Repos Json #fail')
        print(str_json)
        break

    # print(json.dumps(js, indent=4))

    for r in js:
        name = r['name']
        url = r['pulls_url']
        url = url.replace('{/number}','')

        # print('Retrieving', url)
        (str_json, headers) = giturl.urlopen(url)
        # print('Retrieved', len(str_json), 'characters')

        try:
            js = json.loads(str_json)
        except:
            print('Pulls Json #fail')
            print(str_json)
            quit()

        count = len(js)
        # print(name, count)
        pulls[repo+'/'+name] = count

print()
print('Summary:')
count = 0
for (k,v) in pulls.items():
    if v == 0 : count = count + 1
print('Repos without pulls:', count)

count = 0
for (k,v) in pulls.items():
    if v == 0 : continue
    print('Pulls available: ',k,'('+str(v)+')')
    count = count + 1
print('No outstanding pulls')

