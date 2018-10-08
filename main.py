#!/usr/bin/env python3
u"""Exercice de recherche de chemin."""
from breadth_first_search import breadth_first_search
from scraper import Scraper
from problem import Problem
import argparse
import time



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='beaconSystem'
                                     'plotting and Saving')
    parser.add_argument('url1', type=str, help='first url')
    parser.add_argument('url2', type=str, help='second url')
    args = parser.parse_args()
    pb = Problem(args.url1, args.url2)
    print('Searching links between {} and {}.'.format(args.url1, args.url2))
    start = time.time()
    url_list = pb.solve()
    end = time.time()
    print(url_list)
    print(len(url_list))
    print(end - start)
