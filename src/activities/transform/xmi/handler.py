# -*- coding: utf-8 -*-
#
# Copyright 2009: Johannes Raggam, BlueDynamics Alliance
#                 http://bluedynamics.com
# GNU Lesser General Public License Version 2 or later

__author__ = """Johannes Raggam <johannes@raggam.co.at>"""
__docformat__ = 'plaintext'

from agx.core import handler
from agx.io.xml.configure import registerXMLScope
from flavours.xmi2_1 import XMI2_1

from activities.metamodel.elements import Activity
from activities.metamodel.elements import ActivityEdge
from activities.metamodel.elements import ActivityFinalNode
from activities.metamodel.elements import DecisionNode
from activities.metamodel.elements import FlowFinalNode
from activities.metamodel.elements import ForkNode
from activities.metamodel.elements import InitialNode
from activities.metamodel.elements import JoinNode
from activities.metamodel.elements import MergeNode
from activities.metamodel.elements import OpaqueAction
from activities.metamodel.elements import get_element_by_xmiid

import logging
log = logging.getLogger('activities.transform.xmi')

###############################################################################
# Scopes
###############################################################################

# TODO: Better register in zcml?
registerXMLScope('package', 'xmi2act', [
                 '{http://schema.omg.org/spec/UML/2.1.1}Package',
                 '{http://www.eclipse.org/uml2/3.0.0/UML}Package',
                ])
registerXMLScope('packagedElement', 'xmi2act', [XMI2_1.PACKAGED_ELEMENT,])
registerXMLScope('activity_elements', 'xmi2act', [XMI2_1.NODE, XMI2_1.EDGE,])
registerXMLScope('edge', 'xmi2act', [XMI2_1.EDGE,])


###############################################################################
# Handlers
###############################################################################
#xmi_flavor = None

@handler('update_package', 'xmi2act', 'actgenerator', 'package')
def update_package(self, source, target):
    target.xmiid = source.attributes[XMI2_1.XMI_ID]
    target.__name__ = target.xmiid

    #if 'eclipse' in source.__name__:
    #    xmi_flavor = 'eclipse'
    log.info("Package " + target.xmiid + " updated")

# TODO: Better register handler in zcml?
@handler('create_activity', 'xmi2act', 'actgenerator', 'packagedElement')
def create_activity(self, source, target):
    if source.attributes[XMI2_1.TYPE] == XMI2_1.ACTIVITY:
        act = Activity(source.attributes[XMI2_1.NAME])
        act.xmiid = source.attributes[XMI2_1.XMI_ID]
        target[act.xmiid] = act # using xmiid as name to easily reference
                                # to that activity later on.
        log.info("Activity " + target.xmiid + " created")


@handler('create_elements', 'xmi2act', 'actgenerator', 'activity_elements')
def create_elements(self, source, target):
    stype = source.attributes[XMI2_1.TYPE]
    sname = source.attributes[XMI2_1.NAME]
    sxmiid = source.attributes[XMI2_1.XMI_ID]

    # TODO: too hacky...
    if "http://www.eclipse.org/uml2/3.0.0/UML" in source.root.keys()[0]:
        sactref = source.__parent__.attributes[XMI2_1.XMI_ID]
    else:
        sactref = source.attributes[XMI2_1.ACTIVITY_REF]

    factory = None
    if stype == XMI2_1.OPAQUE_ACTION:
        factory = OpaqueAction
    elif stype == XMI2_1.INITIAL_NODE:
        factory = InitialNode
    elif stype == XMI2_1.ACTIVITY_FINAL_NODE:
        factory = ActivityFinalNode
    elif stype == XMI2_1.FLOW_FINAL_NODE:
        factory = FlowFinalNode
    elif stype == XMI2_1.DECISION_NODE:
        factory = DecisionNode
    elif stype == XMI2_1.MERGE_NODE:
        factory = MergeNode
    elif stype == XMI2_1.FORK_NODE:
        factory = ForkNode
    elif stype == XMI2_1.JOIN_NODE:
        factory = JoinNode
    elif stype in (XMI2_1.CONTROL_FLOW, XMI2_1.OBJECT_FLOW):
        factory = ActivityEdge

    if factory:
        target[sactref][sname] = factory()
        target[sactref][sname].xmiid = sxmiid
        log.info(factory.__name__ + " " + target.xmiid + " created")


@handler('edge_connect', 'xmi2act', 'actreferences', 'edge')
def edge_connect(self, source, target):
    """Connects edges to source and target elements.
    """
    sname = source.attributes[XMI2_1.NAME]
    stype = source.attributes[XMI2_1.TYPE]
    ssource = source.attributes[XMI2_1.SOURCE]
    starget = source.attributes[XMI2_1.TARGET]

    # TODO: too hacky...
    if "http://www.eclipse.org/uml2/3.0.0/UML" in source.root.keys()[0]:
        sactref = source.__parent__.attributes[XMI2_1.XMI_ID]
    else:
        sactref = source.attributes[XMI2_1.ACTIVITY_REF]

    if stype in (XMI2_1.CONTROL_FLOW, XMI2_1.OBJECT_FLOW):
        target[sactref][sname].source = get_element_by_xmiid(target, ssource)
        target[sactref][sname].target = get_element_by_xmiid(target, starget)
        log.info("ActivityEdge " + target.xmiid +\
                 " connected with source " + ssource + ", target " + starget)

#