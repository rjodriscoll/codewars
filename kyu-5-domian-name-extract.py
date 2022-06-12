import re 

pref = ['www.', 'https://', 'http://']
def domain_name(url):
    for p in pref:
        url = url.replace(p, "")
    domain = re.findall("^([^.]+)",url)
    return domain[0]