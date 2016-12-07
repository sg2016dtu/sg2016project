from bs4 import BeautifulSoup
import helpers as h
import re
import tags_stripper as ts

def parse_script_list(filename, path):
    all_html = h.open_file(filename, path)
    soup = BeautifulSoup(all_html,'html.parser')
    all_links = soup.find_all(href=re.compile("Script"))
    all_hrefs = []

    for a in all_links[5:len(all_links)]:
        all_hrefs.append(a.get("href"))

    actual_links = []
    for raw_link in all_hrefs:
        temp = raw_link.partition("/Movie Scripts/")[2]
        temp = temp.replace(" ","-")
        temp = temp.replace("-Script", "")
        temp = temp.replace("..", ".")
        temp = temp.replace(":","")
        actual_links.append(temp)
    return actual_links


def parse_one_script(path, filename, output_path):
    all_html = h.open_file(filename,path)
    soup = BeautifulSoup(all_html,'html.parser')
    try:
        script = soup.find_all("pre")[0]
        h.write_to_file(str(script),filename, output_path)
        return None
    except:
        print "Error: no <pre> in", filename
        return filename


def clean_one_script_from_tags(path, filename, output_path):
    h.write_to_file(ts.strip_tags(h.open_file(filename,path)),filename,output_path)

