"""
errors.py module for version_utils
"""


class VersionUtilsError(Exception):
    """Base error class for version_utils exceptions"""
    pass


class RpmError(VersionUtilsError):
    """Error class for the RPM module"""
    pass


class DebError(VersionUtilsError):
    """Error class for the Debian module"""
    pass
