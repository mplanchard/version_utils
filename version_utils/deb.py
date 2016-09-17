"""
Module providing version comparison support for Debian-style packages
and version strings

The documentation for the Debian specification can be found
`here <http://www.fifi.org/doc/debian-policy/policy.html/ch-versions.html>`_.
"""

# Standard library imports
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import logging

# Third party imports

# Local imports
from .common import Epoch, Package, Version


LOG = logging.getLogger(__name__)


def compare_packages(string_a, string_b, arch_provided=True):
    """Compare packages"""


def compare_evrs(evr_a, evr_b):
    """Compare evrs"""


def compare_versions(version_a, version_b):
    """Compare two version strings"""


def package(package_string, arch_included=True):
    """Turn a package string into a Package object"""


def parse_package(package_string, arch_included=True):
    """Parse name, evr, and arch from a package string"""
