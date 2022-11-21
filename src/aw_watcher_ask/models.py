# SPDX-FileCopyrightText: Bernardo Chrispim Baron <bc.bernardo@hotmail.com>
#
# SPDX-License-Identifier: MIT

"""Representations for exchanging data with Zenity and ActivityWatch."""


from enum import Enum


class DialogType(str, Enum):
    entry = "entry"  # Display text entry dialog
    scale = "scale"  # Display scale dialog
    choice = "choice"  # Display choice dialog


