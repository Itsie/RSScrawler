# -*- coding: utf-8 -*-
# RSScrawler - Version 2.0.2
# Projekt von https://github.com/rix1337
# Enthält Code von:
# https://github.com/dmitryint (im Auftrag von https://github.com/rix1337)

def get_first(iterable):
    return iterable and list(iterable[:1]).pop() or None
