#!/usr/bin/env python
# -*- coding: utf-8 -*-

import funciones as fn

inputa=str(sys.argv[1])
file = open(inputa)
text_ph = file.read()
file.close()

fig, Data = fn.distribucion_acento(text_ph)