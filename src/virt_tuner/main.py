#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Authors: Cedric Bosdonnat <cbosdonnat@suse.com>
#
# Copyright (C) 2021 SUSE, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Main executable file which process input arguments
and calls corresponding methods on appropriate object.
"""

import argparse
import gettext
import logging
import sys

import virt_tuner

gettext.bindtextdomain("virt-tuner", "/usr/share/locale")
gettext.textdomain("virt-tuner")
try:
    gettext.install("virt-tuner", localedir="/usr/share/locale")
except IOError:
    import builtins

    builtins.__dict__["_"] = str

logger = logging.getLogger("virt_tuner.main")


def set_logging_conf(loglevel=None):
    """
    Set format and logging level
    """
    # Get logger
    module_logger = logging.getLogger("virt_tuner")

    # Create console handler
    console_handler = logging.StreamHandler()

    # Set logging format
    log_format = "%(levelname)-8s: %(message)s"
    console_handler.setFormatter(logging.Formatter(log_format))

    # Add the handlers to logger
    module_logger.addHandler(console_handler)

    # Set logging level
    module_logger.setLevel(loglevel or logging.INFO)


<<<<<<< HEAD
def main():
=======
def list_templates():
    """
    Print the list of templates to stdout
    """
    print(_("Templates:\n"))
    for name, template in virt_tuner.templates.items():
        print(f" - {name}: {template.description}")


def main(argv):
>>>>>>> f66a4f5 (fixup! Initial commit)
    """
    CLI tool entry point
    """
    parser = argparse.ArgumentParser(
        description=_("VM definition tuner"),
        conflict_handler="resolve",
    )

    parser.add_argument(
        "--version",
        help=_("Print the version"),
        action="version",
        version="%(prog)s " + virt_tuner.__version__,
    )
    parser.add_argument(
        "-d",
        "--debug",
        help=_("Show debug messages"),
        action="store_const",
        dest="loglevel",
        const=logging.DEBUG,
    )

    try:
        args = parser.parse_args(argv)

        # Configure logging lovel/format
        set_logging_conf(args.loglevel)

        sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(0)
    except ValueError as err:
        logging.error(err)
        sys.exit(1)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
