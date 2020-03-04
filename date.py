# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 15:38:13 2020

@author: Eunjung
"""


from datetime import datetime
print (datetime.now().strftime("%d/%m/%Y %Hh%M"))
print (datetime.now().strftime("%A %B %Y")) 


import locale
locale.setlocale(locale.LC_TIME,"") # fuseau horraire 

import time
print (time.strftime("%A %d %B %Y %H:%M:%S")) # %A pour les jours et %B pour les moi