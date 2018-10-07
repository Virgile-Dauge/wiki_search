#!/usr/bin/env python3
from scraper import Scraper

class Problem(object):
    """Specification of our problem for generalised breadth first search."""
    def __init__(self, start_url, goal_url):
        """Saving two urls to link."""
        super(Problem, self).__init__()
        self.start_url = start_url
        self.goal_url = goal_url
        self.scraper = Scraper()
        self.base_url = 'https://fr.wikipedia.org'

    def get_root(self, side='left'):
        """Return the root node aka starting url."""
        if side == 'left':
            return self.start_url
        if side == 'right':
            return self.stop_url

    def is_goal(self, url):
        """Return true if the given url is same as goal_url."""
        return url == self.goal_url

    def get_successors(self, subtree_root):
        """Return list of successors for given address."""
        return self.scraper.scrap(subtree_root)
