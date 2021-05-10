# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 14:20:49 2017

@author: santiago
"""

from openalpr import Alpr

alpr = Alpr("us", "/home/santiago/openalpr/config/alprd.conf", "/home/santiago/openalpr/runtime_data")
if not alpr.is_loaded():
     print("Error loading OpenALPR")

alpr.set_top_n(20)
alpr.set_default_region("md")

results = alpr.recognize_file("/home/santiago/Escritorio/tun.jpg")

i = 0
for plate in results['results']:
     i += 1
     print("Placa #%d" % i)
     print("   %12s %12s" % ("Placa", "% Acierto"))
     for candidate in plate['candidates']:
         prefix = "-"
         if candidate['matches_template']:
             prefix = "*"

         print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))

 # Call when completely done to release memory
alpr.unload()
