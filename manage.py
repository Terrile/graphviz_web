#!/usr/bin/env python
import os
import os.path
import sys
import graphviz_web.settings
loaded = False
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "graphviz_web.settings")
    if os.path.isfile('load.start'):
        graphviz_web.settings.graph.load('graph.txt')
    else:
        open('load.start','a').close()

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
