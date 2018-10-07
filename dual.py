#!/usr/bin/env python3
u"""Generic breadth_first_search algorithm."""
from collections import deque
import time

def breadth_first_search(problem):

    flipflap = True
    solved = False
    # a FIFO open_set
    open_left_set = deque()
    open_right_set = deque()

    # an empty set to maintain visited nodes
    closed_left_set = set()
    closed_right_set = set()

    # a dictionary to maintain meta information (used for path formation)
    # key -> (parent state, action to reach child)
    meta_left = dict()
    meta_right = dict()

    # initialize
    root_left = problem.get_root('left')
    root_right = problem.get_root('right')
    meta_left[root] = (None)
    meta_right[root] = (None)
    open_left_set.append(root_left)
    open_right_set.append(root_right)
    if flipflap:
        flipflap = False
        # For each node on the current level expand and process, if no children
        # (leaf) then unwind
        while not len(open_left_set) == 0:

            subtree_left_root = open_left_set.pop()
            print('subtree_root : ', subtree_left_root)
            # time.sleep(1)
            # We found the node we wanted so stop and emit a path.
            if problem.is_goal(subtree_left_root):
                return construct_path(subtree_left_root, meta)

            # For each child of the current tree process
            for child in problem.get_successors(subtree_left_root):
                # The node has already been processed, so skip over it
                if child in closed_left_set or child in closed_left_set:
                    continue
                else:
                    #TODO check if both sides are reachable if ok, we found path
                    pass

                # The child is not enqueued to be processed, so enqueue this level of
                # children to be expanded
                if child not in open_left_set:
                    # print('child : ', child)
                    meta_left[child] = subtree_left_root  # create metadata for these nodes
                    open_left_set.appendleft(child)              # enqueue these nodes

            # We finished processing the root of this subtree, so add it to the closed
            # set
            closed_left_set.add(subtree_left_root)
    else:
        flipflap = True
# Produce a backtrace of the actions taken to find the goal node, using the
# recorded meta dictionary


def construct_path(state, meta):
    print('Target : {} reached'.format(state))
    action_list = list()

    # Continue until you reach root meta data (i.e. (None, None))
    while meta[state] is not None:
        state = meta[state]
        action_list.append(state)

    action_list.reverse()
    return action_list
