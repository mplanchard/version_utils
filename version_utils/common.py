"""
Module for implementation of functionality common to various package
management systems.
"""

# Standard library imports
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import abc
from logging import getLogger

# Local imports

log = getLogger(__name__)


# Return values:
#   a_newer: a is newer than b, return 1
#   b_newer: b is newer than a, return -1
#   a_eq_b: a and b are equal, return 0
A_NEWER = 1
B_NEWER = -1
A_EQ_B = 0


class Package(object):
    """A class to hold information about a system package

    All parameters except ``name`` are optional and default to None

    :param str name: package name
    :param str epoch: epoch string, default None
    :param str version: version string, default None
    :param str release: release string, default None
    :param str arch: architecture string, default None
    :param str package: original package manager style package string,
        default None
    :ivar str name: package name
    :ivar str epoch: package epoch
    :ivar str version: package version
    :ivar str arch: package architecture
    :ivar tuple evr: a 3-tuple containing (epoch, version, release)
    :ivar tuple info: a 5-tuple containing (name, epoch, version, release,
        architecture)
    :ivar str package: the system-style package string
    """

    def __init__(self, name, epoch=None, version=None, release=None,
                 arch=None, package_str=None):
        self.name = name
        self.epoch = epoch
        self.version = version
        self.release = release
        self.arch = arch
        self.evr = (epoch, version, release)
        self.info = (name, epoch, version, release, arch)
        self.package = package_str

    def __str__(self):
        """Create a string representation of a Package object"""
        return 'Package Object: {0}'.format(self.info)

    def __repr__(self):
        """Full representation of a Package object"""
        return ('Package("{0}", "{1}", "{2}", "{3}", "{4}", '
                '"{5}")'.format(self.name, self.epoch, self.version,
                                self.release, self.arch, self.package))


class Epoch(object):
    """An object to provide epoch parsing and defaults

    :param str epoch: the epoch with which to construct the class
    """

    def __init__(self, epoch):
        self.epoch = str(epoch)

    def __cmp__(self, other):
        a = int(self.epoch)
        b = int(other.epoch)
        if a == b:
            return A_EQ_B
        elif a > b:
            return A_NEWER
        else:
            return B_NEWER

    def __str__(self):
        """The epoch as a string

        The epoch string should be just the epoch integer converted
        to a string, suitable for inclusion in version strings.

        :rtype: str
        """
        return self.epoch

    def __repr__(self):
        """Full representation of an Epoch"""
        return 'Epoch(%s)' % self.epoch


class Version(object):
    """A base class for version classes"""

    __metaclass__ = abc.ABCMeta

    def __init__(self, version_str):
        """Instantiate a Version object

        :param str version_str: the version string to parse
        """
        self.version_string = version_str
        self.epoch, self.version, self.revision = self.parse(version_str)

    @abc.abstractmethod
    def parse(self):
        """Parse the version string and return epoch, version, release

        :returns: a 3-tuple of strings of the form ``(epoch, version,
        release)``
        :rtype: tuple
        """

    @abc.abstractmethod
    def __cmp__(self, other):
        """Compare two version objects

        Return -1 if ``self < other``, 0 if ``self == other``, and 1 if
        ``self > other``
        """

    @abc.abstractmethod
    def __str__(self):
        """Return a string representation of the Version

        The string representation should be suitable for inclusion in
        an official version string
        """

    @abc.abstractmethod
    def __repr__(self):
        """Return a fully-qualified representation of the Version

        The response from ``__repr__`` should be able to be evaluated
        directly with ``eval()`` and return an identical object
        """
