# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class LeaseAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """LeaseAction."""

    ACQUIRE = "acquire"
    AUTO_RENEW = "auto-renew"
    RELEASE = "release"
    ACQUIRE_RELEASE = "acquire-release"


class ListBlobsIncludeItem(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ListBlobsIncludeItem."""

    COPY = "copy"
    DELETED = "deleted"
    METADATA = "metadata"
    SNAPSHOTS = "snapshots"
    UNCOMMITTEDBLOBS = "uncommittedblobs"
    VERSIONS = "versions"
    TAGS = "tags"


class PathExpiryOptions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """PathExpiryOptions."""

    NEVER_EXPIRE = "NeverExpire"
    RELATIVE_TO_CREATION = "RelativeToCreation"
    RELATIVE_TO_NOW = "RelativeToNow"
    ABSOLUTE = "Absolute"


class PathGetPropertiesAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """PathGetPropertiesAction."""

    GET_ACCESS_CONTROL = "getAccessControl"
    GET_STATUS = "getStatus"


class PathLeaseAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """PathLeaseAction."""

    ACQUIRE = "acquire"
    BREAK = "break"
    CHANGE = "change"
    RENEW = "renew"
    RELEASE = "release"


class PathRenameMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """PathRenameMode."""

    LEGACY = "legacy"
    POSIX = "posix"


class PathResourceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """PathResourceType."""

    DIRECTORY = "directory"
    FILE = "file"


class PathSetAccessControlRecursiveMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """PathSetAccessControlRecursiveMode."""

    SET = "set"
    MODIFY = "modify"
    REMOVE = "remove"


class PathUpdateAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """PathUpdateAction."""

    APPEND = "append"
    FLUSH = "flush"
    SET_PROPERTIES = "setProperties"
    SET_ACCESS_CONTROL = "setAccessControl"
    SET_ACCESS_CONTROL_RECURSIVE = "setAccessControlRecursive"
