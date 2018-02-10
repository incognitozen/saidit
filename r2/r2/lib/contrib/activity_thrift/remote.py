#!/usr/bin/env python
#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

from __future__ import print_function
from __future__ import absolute_import

import os
import sys


from . import ActivityService
from . import ttypes

from thrift.util.remote import Function, Remote
FUNCTIONS = {
    'record_activity': Function('record_activity', None, [('ContextID', 'context_id', 'string'), ('VisitorID', 'visitor_id', 'string')]),
    'count_activity': Function('count_activity', 'ActivityInfo', [('ContextID', 'context_id', 'string')]),
    'count_activity_multi': Function('count_activity_multi', 'map<ContextID, ActivityInfo>', [('list<ContextID>', 'context_ids', 'list<ContextID>')]),
    'is_healthy': Function('is_healthy', 'bool', []),
}

if __name__ == '__main__':
    Remote.run(FUNCTIONS, ActivityService, ttypes, sys.argv, default_port=9090)