#!/usr/local/bin/python3.8

import sys
import random
import subprocess as sub
import argparse


def grabs_args():
    parser = argparse.ArgumentParser(description="Select a random thing in a given folder")
    parser.add_argument('path', help='Path of Folder', type=str)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', '--verbose', action='store_true')
    group.add_argument('-q', '--quiet', action='store_true')
    args = parser.parse_args()
    return args


def run_ls(path):
    command = ['ls', path]
    completed_pro = sub.run(command, universal_newlines=True, capture_output=True, text=True)
    stdout = completed_pro.stdout
    files = stdout.split('\n')
    files = [x for x in files if x != ""]  # if file has no name for some reason, remove it.
    return files


def main():
    # grab the first argument
    args = grabs_args()
    path = args.path

    # run the command 'ls', get back list of found stuff:
    files = run_ls(path)

    # -- another way of making the list is: glob.glob(path + "*") -- #

    # print the random thing:
    if not files:
        print("path doesn't exist or it's empty")
        return

    rs = random.choice(files)
    if args.verbose:
        print("Randomly selected thing: %s" % rs)
    elif args.quiet:
        print("%s" % rs)
    else:
        print("random: %s" % rs)


if __name__ == '__main__':
    main()
