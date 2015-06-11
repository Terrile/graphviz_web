#!/usr/bin/env python
import os
import sys
import graphviz_web.settings
loaded = False
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "graphviz_web.settings")
    if loaded==False:
        graphviz_web.settings.graph.load('graph.txt')
        loaded = True
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
