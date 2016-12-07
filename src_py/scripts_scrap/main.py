import scrapper as sc
import helpers as h
import parser as ps
import os
import re


def scrap_all_scripts():

    scripts_filename = "all_scripts_list" # + h.timestamp()

    scripts_path = "raw_html/"
    url_scripts_list = "http://www.imsdb.com/all%20scripts/"

    sc.scrap_page(url_scripts_list, scripts_filename,scripts_path)

    link_prefix = "http://www.imsdb.com/scripts/"
    all_links = ps.parse_script_list(scripts_filename, scripts_path)

    count = 0
    for link in all_links:
        sc.scrap_page(link_prefix + link, link, scripts_path + "raw_scripts/")
        count += 1
        print "Done: ", count, "/", len(all_links), "\n"


def parse_all_scripts():
    raw_scripts_path = "raw_html/raw_scripts/"
    clean_scripts_path = "clean_scripts/with_tags/"
    error_scripts = set()
    for script in os.listdir(raw_scripts_path):
        # determine if the script is there as html; number is in bytes
        if h.determine_file_size(raw_scripts_path, script) > 50000:
            error_scripts.add(ps.parse_one_script(raw_scripts_path, script, clean_scripts_path))
    return error_scripts


def clean_all_scripts():
    scripts_with_tag_path = "clean_scripts/with_tags/"
    clean_scripts_path = "clean_scripts/no_tags/"
    for script in os.listdir(scripts_with_tag_path):
        ps.clean_one_script_from_tags(scripts_with_tag_path, script, clean_scripts_path)


def rename_all_scripts():
    movies = h.read_from_dataset("imdb_dataset_v7.1_6_actors_complete.tsv")
    scripts_no_tag_path = "clean_scripts/no_tags/"
    clean_scripts_path = "clean_scripts/finished_renamed/"
    script_names = os.listdir(scripts_no_tag_path)

    for script in script_names:
        temp = script.replace(".html","").replace("-", " ")
        if re.search(r'\b, The\b', temp):
            temp = temp.replace(",", "")
            temp = temp.partition(" The")[0]
            temp = "The " + temp

        for title in movies:
            jac = h.compute_jaccard_index(title.partition(" (")[0],temp)
            if jac >= 1:
                print jac, title, temp
                h.write_to_file(h.open_file(script, scripts_no_tag_path), title.replace("/","."), clean_scripts_path)

scrap_all_scripts()
error_scripts = parse_all_scripts()
clean_all_scripts()
rename_all_scripts()



