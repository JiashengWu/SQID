#!/usr/bin/python
# -*- coding: utf-8 -*-

# This script retrieves data about the use of classes and properties
# on Wikidata from SPARQL. The results are processed and stored in the
# files properties.json and classes.json. The script must be run in a
# directory that already contains these files (possibly with no content
# other than an empty map {}). Normally, the files are first generated
# by the Java export tool, which provides some statistics that cannot
# be obtained in an acceptable time from SPARQL.

import os
import sys
import logging
import argparse

import sqid

HELPERS_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(HELPERS_DIR, '..', '..', 'src', 'data')
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description='Update statistics data for SQID.')
    parser.add_argument('-o', '--only', dest='only',
                        choices=['properties', 'classes', 'derived'],
                        help='only update statistics for KIND')
    parser.add_argument('--version', action='version',
                        version='sqid-2.0-SNAPSHOT')
    parser.add_argument('--data-path', action='store', dest='path',
                        help='path to data files', default=DATA_DIR)
    parser.add_argument('--no-derived', action='store_false', dest='derived',
			help='Do not compute derived records')

    verb = parser.add_mutually_exclusive_group()
    verb.add_argument('-v', '--verbose', dest='verbose', default=False,
                      action='store_true', help='increase verbosity')
    verb.add_argument('-q', '--quiet', dest='quiet', default=False,
                      action='store_true', help='suppress (some) output')
    verb.add_argument('-l', '--loglevel', dest='loglevel', default='INFO',
                      choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO',
                               'DEBUG'], help='Set the log level')
    args = parser.parse_args()

    if args.verbose:
        loglevel = logging.DEBUG
    elif args.quiet:
        loglevel = logging.WARNING
    else:
        loglevel = args.loglevel

    sqid._setup_default_logger(loglevel=loglevel)  # pylint:disable=protected-access

    if args.only and args.only == 'derived' and not args.derived:
        logger.critical('--no-derived and --only=derived are mutually exclusive')
        sys.exit(1)

    # try to guess the correct directory
    try:
        wd = os.getcwd()
        os.chdir(args.path)

        if not args.only or args.only == 'properties':
            sqid.update_property_records()
        if not args.only or args.only == 'classes':
            sqid.update_class_records()
        if not args.only or args.only == 'derived':
            sqid.update_derived_records()
    finally:
        os.chdir(wd)            # restore previous working directory
