# -*- coding: utf-8; -*-

"""
Copyright (C) 2013 - Ebru Akagündüz <ebru.akagunduz@gmail.com>

This file is part of watchdog-email-notification.

watchdog-email-notification is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

watchdog-email-notification is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>

"""

from distutils.core import setup
import glob

setup(
    name="watchdog-email-notification",
    version="1.0",
    description="Sends email when any file changes in /etc",
    author="Ebru Akagunduz",
    author_email="ebru.akagunduz@gmail.com",
    license="GPLv3",
    data_files=[
        ('/sbin/', glob.glob('file_monitoring.py'))]
)
