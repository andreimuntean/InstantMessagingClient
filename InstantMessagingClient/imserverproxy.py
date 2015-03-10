#!/usr/bin/python2

"""imserverproxy.py: Server proxy module. Provides local functions that execute GET and SET."""

__author__ = 'andrei.muntean.dev@gmail.com (Andrei Muntean)'

import urllib2
from urllib import quote

class IMServerProxy:
    def __init__(self, url):
        self.url = url

        if not self['message_count']:
            self['message_count'] = '0'

    def __getitem__(self, key):
        """Gets the value to which the specified key is mapped."""

        return urllib2.urlopen(self.url + '?action=get&key=' + quote(key)).read()

    def __setitem__(self, key, value):
        """Maps a key to the specified value."""

        urllib2.urlopen(self.url + '?action=set&key=' + quote(key) + '&value=' + quote(value))

    def __delitem__(self, key):
        """Deletes the value to which the specified key is mapped."""

        urllib2.urlopen(self.url + '?action=unset&key=' + quote(key))

    def clear(self):
        """Deletes all the keys stored on the server."""

        urllib2.urlopen(self.url + '?action=clear')

    def keys(self):
        """Returns a list of all the keys stored on the server."""

        return urllib2.urlopen(self.url + '?action=keys').read().splitlines()