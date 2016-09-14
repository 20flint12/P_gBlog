#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import imp


print __name__
print('-' * 40)


# PATH_MAIN_DIR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
MAIN_DIR = os.path.dirname(os.path.abspath(__file__)) + "/"
MAIN_DIR_UP = os.path.abspath(os.path.join(__file__, "../..")) + "/"
print MAIN_DIR, "- located main_NHM.py"
print MAIN_DIR_UP, "- one up dir "
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def dynamic_importer(name, in_path):
    """
    Dynamically imports modules
    """
    print "search path:", in_path
    try:
        fp, pathname, description = imp.find_module(name, [in_path])
    except ImportError:
        print "unable to locate module: " + name
        return None

    try:
        example_package = imp.load_module(name, fp, pathname, description)
    except Exception, e:
        print e

    return example_package



# -----------------------------------------------------------------------------
CONFIG_DJG = dynamic_importer("config_DJG", MAIN_DIR_UP + "djangogirls/")
# print "@@@ CONFIG_DJG=", CONFIG_DJG

# -----------------------------------------------------------------------------
# CONNECTION_NHM = dynamic_importer("connection_setting", MAIN_DIR_UP + "M_common/")
# print "@@@ CONNECTION_NHM=", CONNECTION_NHM

# COMMMANDS_SLIP = dynamic_importer("commands_slip", MAIN_DIR_UP + "M_common/")
# print "@@@ COMMMANDS_SLIP=", COMMMANDS_SLIP
#
# HW_PARAM = dynamic_importer("HW_param", MAIN_DIR_UP + "M_common/")
# print "@@@ HW_PARAM=", HW_PARAM

# -----------------------------------------------------------------------------
# READ_CONFIG_SVR = dynamic_importer("read_config_SVR", MAIN_DIR_UP + "P_scheduler_emu/")
# print "@@@ READ_CONFIG_SVR=", READ_CONFIG_SVR
#
# ROUTINES_SVR = dynamic_importer("routines_SVR", MAIN_DIR_UP + "P_scheduler_emu/")
# print "@@@ ROUTINES_SVR=", ROUTINES_SVR










