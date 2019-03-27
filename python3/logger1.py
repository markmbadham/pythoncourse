#!/usr/bin/env python3

import logging as log
import traceback as tb
FORMAT = '%(asctime)s:%(levelname)10s:%(message)s'
log.basicConfig(format=FORMAT,filename='logger.log', level=log.DEBUG)
log.debug("debug message")
log.warn("warning message")
try:
    1/0
except ZeroDivisionError:
    log.error(tb.format_exc().replace('\n','-'))
