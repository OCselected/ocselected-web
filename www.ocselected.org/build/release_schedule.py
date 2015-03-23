#!/usr/bin/python
# -*- coding: utf-8 -*-
# This script will parse the f-XX-key-milestones.tjx file and retrieve three relevant
# dates: Alpha Release Public Availability, Beta Release Public Availability and Final Release Public Availability.


import urllib2
from urllib2 import HTTPError
from urllib2 import URLError
from StringIO import StringIO
import gzip
from lxml import etree
import cPickle, os

def parse(cache, r):
    root = etree.fromstring(cache)
    date={}

    alpha_release = root.xpath('//task[@id="f' + r + '.TestingPhase.alpha.alpha_drop"]/taskScenario/start/@humanReadable')
    beta_release = root.xpath('//task[@id="f' + r + '.TestingPhase.beta.beta_drop"]/taskScenario/start/@humanReadable')
    final_release = root.xpath('//task[@id="f' + r + '.LaunchPhase.final"]/taskScenario/start/@humanReadable')


    try:
        date[r] = {'alpha':alpha_release[0], 'beta':beta_release[0], 'final':final_release[0]}
        return date
    except IndexError:
        return {}


def schedule(release):
    date={}
    ec = None
    cachefile = os.path.join(os.getcwd(), 'build/schedule.cache')


    if os.path.isfile(cachefile):
        f = open(cachefile)
        try:
            ec = cPickle.load(f)
        except:
            pass
        f.close()

    if ec is not None:
        date = parse(ec, release)
        if release in date:
            return date

    # We need to generate the cache!
    # Download the schedule
    try:
        u = urllib2.urlopen('http://fedorapeople.org/groups/schedule/f-' + release + '/f-' + release + '-key-milestones.tjx')
    except HTTPError:
        date[release] = {'alpha':'2014-jan-01', 'beta':'2014-jan-01', 'final':'2014-jan-01'}
        return date

    except URLError:
        date[release] = {'alpha':'2014-jan-01', 'beta':'2014-jan-01', 'final':'2014-jan-01'}
        return date

    # Release is already present in date if we got HTTPError
    if not release in date:
        buf = StringIO(u.read())
        f = gzip.GzipFile(fileobj=buf)
        data = f.read().strip() # looks like there is a leading space in the file

        f = open(cachefile, 'w')
        cPickle.dump(data, f)
        f.close()

        return parse(data, release)
