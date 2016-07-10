#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from datetime import *

from django.core.mail import send_mail


def my_email(str_subject, str_body, list_emails):

    try:
        send_mail(str_subject, str_body,
                  'astroreminder@gmail.com',
                  list_emails,  # ['20flint12@gmail.com','380688845064@sms.kyivstar.net'],
                  fail_silently=False,
                  html_message=str_body)
    except:
        str_res = "Unexpected error:" + str(sys.exc_info()[0]) + str(sys.exc_info()[1])
        print str_res
        # sys.exit()


###############################################################################
###############################################################################
###############################################################################


if __name__ == '__main__':

    email_reminder()















