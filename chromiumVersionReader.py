import urllib2
import json

def readRawRevisionData(url='http://omahaproxy.appspot.com/all.json'):
    '''Retreives a JSON array of all revisions number for all Chromium builds'''
    response = urllib2.urlopen(url)
    return json.load(response)

    
def findVersionForOs(osRevisions, os):
    for revisions in osRevisions:
        if revisions['os'] == os:
            return revisions['versions']

    return None


def findRevisionForChannel(revisions, channel):
    for revision in revisions:
        if revision['channel'] == channel:
            return revision['branch_revision']
    

def findRevisionForOSAndChannel(os, channel, url='http://omahaproxy.appspot.com/all.json'):
    if len(os) == 0:
        os = 'win'

    if len(channel) == 0:
        channel = 'stable'

    data = readRawRevisionData(url)
    version = findVersionForOs(data, os)

    if version == None:
        return ''

    return findRevisionForChannel(version, channel)

    
if __name__ == '__main__' :
    print findRevisionForOSAndChannel()
