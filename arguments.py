import argparse, sys
from os.path import exists

def parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('input', help='input file')
    parser.add_argument('user_output', help='user output file')
    parser.add_argument('judge_output', help='judge output file')

    args = parser.parse_args()
    _validate(args)

    return args

def _validate(args):
    try:
        inp, userOut, judgeOut = args.input, args.user_output, args.judge_output
    except ValueError:
        print('Internal error parsing input')
        return False

    missingFiles = []
    if not exists(inp):
        missingFiles.append('input')
    if not exists(userOut):
        missingFiles.append('user_output')
    if not exists(judgeOut):
        missingFiles.append('judge_output')

    if missingFiles:
        print('Error parsing input files')
        print('The following files are missing or invalid:')
        for f in missingFiles:
           print('\t' + f)

        sys.exit(1)
