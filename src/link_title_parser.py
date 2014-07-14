# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 14:35:41 2014

@author: Robb
"""


import os
#import bs4 #beautifulsoup4
import bs4
from bs4 import BeautifulSoup
import itertools

def find_link_titles(path):
    '''finds all of the link titles'''
    soup = BeautifulSoup(open(path,'r'))
    links = soup.find_all('a')
    return (title.string.strip() for link in links for title in link.find_all('h1') if 'title' in title.get('class') and title.string is not None)
    
def find_links(path):
    '''finds all the links'''
    soup = BeautifulSoup(open(path,'r'))
    return soup.find_all('a')

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

##%% npr
#site = 'npr'
#
#webpages = filter(lambda x: x.startswith(site), os.listdir(data_loc))
#
#webpage = webpages[0]
#
#soup = BeautifulSoup(open(os.path.join(data_loc,webpage),'r'))
#
##links = soup.find_all('a')
###data_metrics_links = [link for link in links if 'data-metrics' in link.attrs]
##link_titles = [title.string.strip() for link in links for title in link.find_all('h1') if 'title' in title.get('class') and title.string is not None]
###link_teasers = [teaser.string.strip() for link in links for teaser in link.find_all('p') if 'teaser' in teaser.get('class') and teaser.string is not None]
#
#
#
##links = find_tags([soup],'a')
##titles = find_tags(links,'h1','class',['title'])
##link_titles = get_strings(titles)
###[c.strip() for link_title in link_titles for c in link_title.children if isinstance(c,bs4.element.NavigableString)]
#
#parse_rules = [dict([('tag_names','a')]),
#               dict([('tag_names','h1'),('attr_name','class'),('attr_vals',['title'])])]
#
#link_titles = apply_parse_rules([soup], parse_rules)

##%% for cnn
#site = 'cnn'
#
#webpages = filter(lambda x: x.startswith(site), os.listdir(data_loc))
#
#webpage = webpages[0]
#soup = BeautifulSoup(open(os.path.join(data_loc,webpage),'r'))
#
##keep_attr = ['t1',
## 'THE LATEST',
## 'OPINION',
## 'MORE TOP STORIES',
## 'IN CASE YOU MISSED IT',
## 'C1.5Top',
## 'C2']
##tag_names = 'div'
##attr_name = 'data-vr-zone'
##sub_tag_names = 'a'
##tags = [tag for tag in soup.find_all(tag_names) if attr_name in tag.attrs and tag.get(attr_name) in keep_attr]
##link_titles = [sub_tag.string for tag in tags for sub_tag in tag.find_all(sub_tag_names) if sub_tag.string is not None]
#
##divs = find_tags([soup],'div','data-vr-zone',['t1',
##                                              'THE LATEST',
##                                              'OPINION',
##                                              'MORE TOP STORIES',
##                                              'IN CASE YOU MISSED IT',
##                                              'C1.5Top',
##                                              'C2'])
##links = find_tags(divs,'a')
##link_titles = get_strings(links)
#
#parse_rules = [dict([('tag_names','div'),('attr_name','data-vr-zone'),('attr_vals',['t1','THE LATEST','OPINION','MORE TOP STORIES','IN CASE YOU MISSED IT','C1.5Top','C2'])]),
#               dict([('tag_names','a')])]
#
#link_titles = apply_parse_rules([soup], parse_rules)

##%% for bbcnews
#site = 'bbcnews'
#
#webpages = filter(lambda x: x.startswith(site), os.listdir(data_loc))
#
#webpage = webpages[0]
#soup = BeautifulSoup(open(os.path.join(data_loc,webpage),'r'))
#
###[c for link in soup.find_all('a') for c in link.contents if 'class' in link.attrs and 'story' in link.get('class') and isinstance(c,bs4.element.NavigableString)]
##links = [link for link in soup.find_all('a') if 'class' in link.attrs and 'story' in link.get('class')]
##link_titles = [c.strip() for link in links for c in link.children if isinstance(c,bs4.element.NavigableString)]
#
##links = find_tags([soup],'a','class',['story'])
##link_titles = get_strings(links)
#
#parse_rules = [dict([('tag_names','a'),('attr_name','class'),('attr_vals',['story'])])]
#
#link_titles = apply_parse_rules([soup], parse_rules)

##%% abcnews
#site = 'abcnews'
#
#webpages = filter(lambda x: x.startswith(site), os.listdir(data_loc))
#
#webpage = webpages[0]
#soup = BeautifulSoup(open(os.path.join(data_loc,webpage),'r'))
#
##div class ffl_wrapper
##div class midcontainer
#
##divs = find_tags([soup],'div','class',['midcontainer'])
##links = find_tags(divs,'a')
##link_titles = get_strings(links)
#
#parse_rules = [dict([('tag_names','div'),('attr_name','class'),('attr_vals',['midcontainer'])]),
#               dict([('tag_names','a')])]
#
#link_titles = apply_parse_rules([soup], parse_rules)

##%% wired
#site = 'wired'
#
#webpages = filter(lambda x: x.startswith(site), os.listdir(data_loc))
#
#webpage = webpages[0]
#soup = BeautifulSoup(open(os.path.join(data_loc,webpage),'r'))
#
#
##div class headline
##div class feed-content
#
#parse_rules = [dict([('tag_names','div'),('attr_name','class'),('attr_vals',['headline','feed-content'])]),
#               dict([('tag_names','a')])]
#
#link_titles = apply_parse_rules([soup], parse_rules)
#%% data write out

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
    ])

for site, parse_rules in site_to_parse_rules.iteritems():
    webpages = filter(lambda x: x.startswith(site), os.listdir(data_loc))
    soups = (BeautifulSoup(open(os.path.join(data_loc,webpage),'r')) for webpage in webpages)
    
    link_titles = list(set(apply_parse_rules(soups, parse_rules)))
    
    
#link_titles = list(set(link_title for webpage in webpages for link_title in find_link_titles(os.path.join(data_loc,webpage))))
#
    with open(os.path.join(data_loc,site+'_link_titles.txt'),'w') as f_out:
        for title in link_titles:
            title = title.replace(u'\u200b','')
            f_out.write(title+os.linesep)
