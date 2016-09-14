#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# linux hostname
HOSTNAME = os.uname()[1]
print "HOSTNAME   :", HOSTNAME
# -----------------------------------------------------------------------------


# GIT_BRANCH = "development"
GIT_BRANCH = "plekhanovskaya121"

BUILD_SET = {

    "plekhanovskaya121":
        [
            'plechan121@gmail.com', # receiver email
            '',                     # color
        ],
    "development":
        [
            '20flint12@gmail.com',
            #-------------------------------
        ],
}

BUILDING_EMAIL = BUILD_SET[GIT_BRANCH][0]

print "BUILDING_EMAIL=", BUILDING_EMAIL