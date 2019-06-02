#!/usr/bin/env python3.7
import argparse
import sys
import json
from collections import defaultdict

def read_args():
    parser = argparse.ArgumentParser(description='Format output of pkg_admin audit')
    parser.add_argument('--outfile', type=str, dest="output_file")
    parser.add_argument('--fmt', type=str, choices=['json','csv'], default='csv')

    return parser.parse_args()

def format_data(input_data: str, fmt_json: bool = False):
    data_dict = defaultdict(list)

    if fmt_json:
        for line in input_data:
            data_dict[''.join(line.strip().split()[1:2])].append(
                {"vuln":line.strip().split()[4:5],"url":line.split()[-1:]})

        print(json.dumps(data_dict))


    else:
        for line in input_data:
            print(''.join(line.strip().split()[1:2]), end=",")
            print(''.join(line.strip().split()[4:5]), end=",")
            print(''.join(line.strip().split()[-1:]))

def main():
    args = read_args()
    print(args)

    # sys.stdin.isatty() returns a False if there is something in stdin, i.e. piped in
    if sys.stdin.isatty():
        print("There is no standard in data. Pipe the output of a file to this script.")
        print(f"Example: pkg_audit | {sys.argv[0]}")
    else:
        data = sys.stdin.readlines()
        format_data(input_data = data, fmt_json = True)

if __name__ == "__main__":
    main()
