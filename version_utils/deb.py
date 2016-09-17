"""
Module providing version comparison support for Debian-style packages
and version strings

The documentation for the Debian specification can be found
`here <https://www.debian.org/doc/debian-policy/ch-controlfields.html>`_
"""

# Standard library imports
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import logging

# Third party imports

# Local imports
from . import _parse as parse
from .common import Epoch, Package, Version
from .errors import DebError


DEFAULT_DELIMITER = ' '
DEFAULT_EPOCH = '0'
DEFAULT_REVISION = '0'
log = logging.getLogger(__name__)


def compare_packages(string_a, string_b, arch_provided=True):
    """Compare packages"""


def compare_evrs(evr_a, evr_b):
    """Compare evrs"""


def compare_versions(version_a, version_b):
    """Compare two version strings"""
    if version_a == version_b:
        return


def package(package_string, arch_included=True, delimiter='_'):
    """Turn a package string into a Package object"""


def parse_package(package_string, arch_included=True, delimiter='_'):
    """Parse name, evr, and arch from a package string"""


def pop_epoch(version):
    """Get the epoch and strip it from the version string

    If no epoch is present, return ``DEFAULT_EPOCH`` (``'0'``)

    :param str version: a debian version string, optionally
        containing epoch and revision information

    :return: a 2-tuple of the form ``epoch, rest`` where ``epoch`` is
        the string epoch and ``rest`` is the version string with the
        epoch prefix removed, if it was present
    :rtype: typing.Tuple[str, str]
    """
    log.debug('epoch_from_version(%s)', version)
    colon_index = version.find(':')
    epoch = version[:colon_index] if colon_index != -1 else DEFAULT_EPOCH
    log.debug('got epoch: %s', epoch)
    rest = version[colon_index + 1:] if colon_index != -1 else version
    log.debug('remainder of string: %s', version)
    return epoch, rest


def pop_revision(version):
    """Return the revision from a version string

    :param str version: a debian version string, optionally
        containing epoch and revision information
    """
    log.debug('revision_from_version(%s)', version)
    dash_index = version.rfind('-')
    rev = version[dash_index + 1:] if dash_index != -1 else DEFAULT_REVISION
    log.debug('got revision: %s', rev)
    rest = version[:dash_index] if dash_index != -1 else version
    log.debug('remainder of string: %s', rest)
    return rev, rest


class DebVersion(Version):
    """Debian Version objects"""

    def parse(self):
        """Parse the version string and return epoch, version, release

        :returns: a 3-tuple of strings of the form ``(epoch, version,
        release)``
        :rtype: tuple
        """
        log.debug('DebVersion.parse()')
        epoch, version = pop_epoch(self.version_string)
        revision, version = pop_revision(version)
        return epoch, version, revision

    def __str__(self):
        """Return a string representation of the Version

        The string representation should be suitable for inclusion in
        an official version string

        :rtype: str
        """
        return '%s:%s-%s' % (self.epoch, self.version, self.revision)

    def __repr__(self):
        """Return a fully-qualified representation of the Version

        The response from ``__repr__`` should be able to be evaluated
        directly with ``eval()`` and return an identical object

        :rtype: str
        """
        return 'DebVersion(%s:%s-%s)' % (
            self.epoch, self.version, self.revision
        )


class DebPackage(Package):
    """Debian Package objects"""

    def __init__(self, name, epoch=None, version=None, revision=None,
                 arch=None, package_str=None):
        self.release = revision  # For compatibility with super class
        super(DebPackage, self).__init__(
            name, epoch=epoch, version=version, release=revision,
            arch=arch, package_str=package_str
        )
