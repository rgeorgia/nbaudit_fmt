#!/usr/bin/env python3.7
import argparse
import sys
import json
import pprint
from collections import defaultdict


def read_args():
    parser = argparse.ArgumentParser(description='Format output of pkg_admin audit')
    parser.add_argument('--outfile', type=str, dest="output_file")
    parser.add_argument('--fmt', type=str, choices=['json', 'csv'], default='csv')

    return parser.parse_args()


def write_to_screen(input_data: str, fmt_json: bool):
    data_dict = {}

    if fmt_json:
        pp = pprint.PrettyPrinter(indent=4, depth=4)
        for line in input_data:
            data_dict[''.join(line.strip().split()[1:2])] = {"vuln": line.strip().split()[4:5],
                                                             "url": line.split()[-1:]}

    else:
        for line in input_data:
            print(''.join(line.strip().split()[1:2]), end=",")
            print(''.join(line.strip().split()[4:5]), end=",")
            print(''.join(line.strip().split()[-1:]))


def write_file(input_data: str, fmt_json: bool, filename: str):
    pass


def main():
    args = read_args()
    fmt_json: bool = False

    if args.fmt.lower() == 'json':
        fmt_json = True

    # sys.stdin.isatty() returns a False if there is something in stdin, i.e. piped in
    if sys.stdin.isatty():
        print("There is no standard in data. Pipe the output of a file to this script.")
        print(f"Example: pkg_audit | {sys.argv[0]}")
        sys.exit(1)
    else:
        data = sys.stdin.readlines()

    if args.output_file:
        write_file(input_data=data, fmt_json=fmt_json, filename=args.outfile)
    else:
        write_to_screen(input_data=data, fmt_json=fmt_json)


if __name__ == "__main__":
    main()
