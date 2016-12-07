import urllib2, time
from random import randint
import helpers as h


def scrap_page(url, filename, path_to_save):
    try:
        print "Request to:", url
        url_response = urllib2.urlopen(url)
    except urllib2.HTTPError as e:
        print "Error scrapping:", e
        return
    url_html = url_response.read()
    h.write_to_file(url_html, filename, path_to_save)
    time.sleep(randint(5, 10))