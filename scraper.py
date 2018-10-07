#!/usr/bin/env python3
u"""Wikipédia articles scraper."""
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import re

class Scraper(object):
    """docstring for Scrapper."""
    base_url = 'https://fr.wikipedia.org'
    def __init__(self):
        """Coucou."""
        super(Scraper, self).__init__()
    def simple_get(self, url):
        """
        Attempts to get the content at `url` by making an HTTP GET request.
        If the content-type of response is some kind of HTML/XML, return the
        text content, otherwise return None.
        """
        try:
            with closing(get(url, stream=True)) as resp:
                if self.is_good_response(resp):
                    return resp.content
                else:
                    return None

        except RequestException as e:
            print('Error during requests to {0} : {1}'.format(url, str(e)))
            return None

    def is_good_response(self, resp):
        """
        Returns True if the response seems to be HTML, False otherwise.
        """
        content_type = resp.headers['Content-Type'].lower()
        return (resp.status_code == 200
                and content_type is not None
                and content_type.find('html') > -1)

    def filter_url(self, href):
        return href and re.compile('/wiki/').match(href) and not re.compile(":").search(href)

    def scrap(self, url, base_url='https://fr.wikipedia.org'):
        # content = BeautifulSoup(self.simple_get(url), 'lxml').find()
        # res = list([])
        # for link in BeautifulSoup(scraper.simple_get(url), 'html.parser').find_all(href=self.filter_url):
        #     url = link.get('href')
        #     if url not in self.history:
        #         self.history.add(url)
        #         res.append(url)
        # return res
        return [link.get('href') for link in BeautifulSoup(self.simple_get(base_url + url), 'lxml').find(id='mw-content-text').find_all(href=self.filter_url)]
