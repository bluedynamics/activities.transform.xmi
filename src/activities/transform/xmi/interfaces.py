# -*- coding: utf-8 -*-
#
# Copyright 2009: Johannes Raggam, BlueDynamics Alliance
#                 http://bluedynamics.com
# GNU Lesser General Public License Version 2 or later

__author__ = """Johannes Raggam <johannes@raggam.co.at>"""
__docformat__ = 'plaintext'

from zope.interface import Interface

class IXMIFlavour(Interface):
    """Holds all information relevant to the different flavors of XMI, such as
    its versions: 1.0, 1.1, 1.2, 2.1
    """