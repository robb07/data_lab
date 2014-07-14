# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 14:35:41 2014

@author: Robb
"""


import os
import bs4


def find_tags(soups, tag_names, attr_name=None, attr_vals=[]):
    '''Finds all tags with name in tag_names in the soup_list and filters by the attribute name and allowed values'''
    
    if attr_name is None:
        return (tag for soup in soups for tag in soup.find_all(tag_names))
    elif attr_name == 'class':
        return (tag for soup in soups for tag in soup.find_all(tag_names) if attr_name in tag.attrs and any([attr_val in attr_vals for attr_val in tag.get(attr_name)]))
    else:
        return (tag for soup in soups for tag in soup.find_all(tag_names) if attr_name in tag.attrs and tag.get(attr_name) in attr_vals)

def get_strings(tags):
    '''Gets the string child for each tag'''
    return (c.strip() for tag in tags for c in tag.children if isinstance(c,bs4.element.NavigableString))
    
def apply_parse_rules(soups, rule_dicts):
    '''Uses the keywords in each dicitonary in the rule_dicts to parse the soups'''
    tags = soups
    for rules in rule_dicts:
        tags = find_tags(tags, **rules)
    return get_strings(tags)

data_loc = 'D:/HTML_dump'

#{'abcnews',
# 'bbc_',
# 'bbcnews',
# 'cbsnews',
# 'cnn',
# 'jezebel',
# 'msnbc',
# 'nbcnews',
# 'npr',
# 'reddit',
# 'wired'}


site_to_parse_rules = dict([
    ('npr',     [dict([('tag_names','a')]),
                 dict([('tag_names','h1'),('attr_name','class'),('attr_vals',['title'])])]),
    ('cnn',     [dict([('tag_names','div'),('attr_name','data-vr-zone'),('attr_vals',['t1','THE LATEST','OPINION','MORE TOP STORIES','IN CASE YOU MISSED IT','C1.5Top','C2'])]),
                 dict([('tag_names','a')])]),
    ('bbcnews', [dict([('tag_names','a'),('attr_name','class'),('attr_vals',['story'])])]),
    ('abcnews', [dict([('tag_names','div'),('attr_name','class'),('attr_vals',['midcontainer'])]),
                 dict([('tag_names','a')])]),
    ('wired',   [dict([('tag_names','div'),('attr_name','class'),('attr_vals',['headline','feed-content'])]),
                 dict([('tag_names','a')])]),
    ('cbsnews', [dict([('tag_names',['h3','h4']),('attr_name','class'),('attr_vals',['title'])])]),
    ('reddit',  [dict([('tag_names','a'),('attr_name','class'),('attr_vals',['title'])])]),
    ])

bad_unicode = [u'\u200b',u'\xe1',u'\u2019',u'\u2018',
                u'\xab',
                u'\u2013',
                u'\u201c',
                u'\u201c',
                u'\xe5',
                u'\u2013',
                u'\u201c',
                u'\xbb',
                u'\xd7',
                u'\xd7',
                u'\u201c',
                u'\xe3',
                u'\u201c',
                u'\u2013',
                u'\u272e']

for site, parse_rules in site_to_parse_rules.iteritems():
    webpages = filter(lambda x: x.startswith(site), os.listdir(data_loc))
    soups = (bs4.BeautifulSoup(open(os.path.join(data_loc,webpage),'r')) for webpage in webpages)
    
    link_titles = list(set(apply_parse_rules(soups, parse_rules)))
    
    
    with open(os.path.join(data_loc,site+'_link_titles.txt'),'w') as f_out:
        for title in link_titles:
            for c in bad_unicode:
                title = title.replace(c,'')
            try:
                f_out.write(title+os.linesep)
            except UnicodeEncodeError as e:
                print "UnicodeEncodeError: {0!r}".format(e)
