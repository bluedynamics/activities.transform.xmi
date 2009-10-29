# -*- coding: utf-8 -*-
#
# Copyright 2009: Johannes Raggam, BlueDynamics Alliance
#                 http://bluedynamics.com
# GNU Lesser General Public License Version 2 or later

__author__ = """Johannes Raggam <johannes@raggam.co.at>"""
__docformat__ = 'plaintext'

from zope.interface import implements
from agx.core.interfaces import ITransform
from agx.io.xml import XMLFactory
from flavours.xmi2_1 import XMI2_1

from activities.metamodel.elements import Package

class XMI2Act(object):
    """XMI to Activities source and target factory.
    """
    implements(ITransform)

    def __init__(self, name):
        self.name = name

    def source(self, path):
        factory = XMLFactory()
        xml = factory(path, XMI2_1.XMI_ID)
        return xml

    def target(self, dummyname=""):
        """Dummyname is not used but required to comply with interface def.
        Activities are collected in the dictionary {xmiid: activity}.
        """
        return Package()