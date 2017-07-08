# -*- encoding: utf-8 -*-
import argparse
import sys

print('hello world')

import gi
from gi.repository import GLib

from .player import GstPlayer
p = GstPlayer('dumdum')
p.play(sys.argv[1])

mainloop = GLib.MainLoop()
mainloop.run()
