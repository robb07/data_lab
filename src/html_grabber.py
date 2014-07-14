'''
Grabs HTML pages and saves them to disk periodically

Created on Jun 18, 2014

@author: Robb
'''

import urllib2
import time

if __name__ == '__main__':
    webpages = [('cnn_{0}.html','http://www.cnn.com/'),
                ('wired_{0}.html','http://www.wired.com/'),
                ('npr_{0}.html','http://www.npr.org/'),
                ('foxnews_{0}.html','http://www.foxnews.com/'),
                ('msnbc_{0}.html','http://www.msnbc.com/'),
                ('reddit_{0}.html','http://www.reddit.com/'),
                ('jezebel_{0}.html','http://jezebel.com/'),
                ('nbcnews_{0}.html','http://www.nbcnews.com/'),
                ('abcnews_{0}.html','http://abcnews.go.com/'),
                ('cbsnews_{0}.html','http://www.cbsnews.com/'),
                ('bbc_{0}.html','http://www.bbc.com/'),
                ('bbcnews_{0}.html','http://www.bbc.com/news/')]
    
    folder = 'D:/HTML_dump/'
    with open(folder + 'dictionary.txt', 'w') as f_out:
        f_out.writelines((filename + '\t' + url + '\n' for filename, url in webpages))
    
    #DELAY = 5#seconds
    #DELAY = 60#seconds
    DELAY = 60*60#seconds
    
    while True:
        timestamp = time.strftime('%Y_%m_%d_%H_%M_%S')
        print 'Grabbing at {0}'.format(timestamp)
        
        for filename, url in webpages:
            try:
                resource = urllib2.urlopen(url)
                
                html = resource.read()
                with open(folder+filename.format(timestamp),'w') as f_out:
                    f_out.writelines(html)
            except:
                print 'Error with:', filename.format(timestamp), url
        
        print 'Waiting...'
        time.sleep(DELAY)
        