# -*- coding: utf-8 -*-
#
# Copyright 2009: Johannes Raggam, BlueDynamics Alliance
#                 http://bluedynamics.com
# GNU Lesser General Public License Version 2 or later

__author__ = """Johannes Raggam <johannes@raggam.co.at>"""
__docformat__ = 'plaintext'

from zope.interface import implements
from activities.transform.xmi.interfaces import IXMIFlavour

class XMI2_1(object):

    implements(IXMIFlavour)

    PACKAGED_ELEMENT = "packagedElement"
    NODE = "node"
    EDGE = "edge"

    XMI_ID = "{http://schema.omg.org/spec/XMI/2.1}id"
    TYPE = "{http://schema.omg.org/spec/XMI/2.1}type"
    NAME = "name"

    SOURCE = "source"
    TARGET = "target"
    ACTIVITY_REF = "activity"

    ACTIVITY = "uml:Activity"
    OPAQUE_ACTION = "uml:OpaqueAction"

    INITIAL_NODE = "uml:InitialNode"
    ACTIVITY_FINAL_NODE = "uml:ActivityFinalNode"
    FLOW_FINAL_NODE = "uml:FlowFinalNode"

    DECISION_NODE = "uml:DecisionNode"
    MERGE_NODE = "uml:MergeNode"
    FORK_NODE = "uml:ForkNode"
    JOIN_NODE = "uml:JoinNode"

    CONTROL_FLOW = "uml:ControlFlow"
    OBJECT_FLOW = "uml:ObjectFlow"


    def __init__(self, **kw):
        self.__dict__.update(kw)