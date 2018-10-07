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
    # parser.add_argument('-o','--outputfile', help='output for saving file')
    # parser.add_argument('-d','--dimension', help='2D or 3D plotting', default='2d', choices=['2d','3d'])
    # parser.add_argument('-m','--mode', help='mode selection', default='single', choices=['single','surface'])
    # parser.add_argument('-a','--animate', help='toggle animation', default=False,type=bool)
    args = parser.parse_args()
    pb = Problem(args.url1, args.url2)
    print('Searching links between {} and {}.'.format(args.url1, args.url2))
    start = time.time()
    url_list = breadth_first_search(pb)
    end = time.time()
    print(url_list)
    print(len(url_list))
    print(end - start)
