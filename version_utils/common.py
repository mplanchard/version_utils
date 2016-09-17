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

LOG = getLogger(__name__)


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

    :param int epoch_default: the default value for epoch if none is
        provided
    """

    def __init__(self, epoch, epoch_default=0):
        self.epoch_default = epoch_default
        self.epoch = self.parse(epoch)

    def parse(self, epoch):
        """Parse an epoch based on ``default_epoch``"""
        if epoch is None or epoch == '':
            return self.epoch_default
        return int(epoch)

    def to_string(self):
        """Return the epoch as a string

        Provided as a means of explicitly accessing implicit string
        conversion of the Epoch class
        """
        return self.__str__()

    def __str__(self):
        """The epoch as a string

        The epoch string should be just the epoch integer converted
        to a string, suitable for inclusion in version strings.

        :rtype: str
        """
        return str(self.epoch)

    def __repr__(self):
        """Full representation of an Epoch"""
        return (
            'Epoch(%s, epoch_default=%s)' % (self.epoch, self.epoch_default)
        )


class Version(object):
    """A base class for classes providing version parsing & defaults"""

    __metaclass__ = abc.ABCMeta

    def __init__(self, version):
        """Instantiate a Version object

        :param str version: the version string to parse
        """
        pass

    @abc.abstractmethod
    def parse(self):
        """Parse the version string"""

    @abc.abstractmethod
    def __str__(self):
        """Return a string representation of the Version

        The string representation should be suitable for inclusion in
        an official Debian version string
        """

    @abc.abstractmethod
    def __repr__(self):
        """Return a fully-qualified representation of the Version

        The response from ``__repr__`` should be able to be evaluated
        directly with ``eval()`` and return an identical object
        """
