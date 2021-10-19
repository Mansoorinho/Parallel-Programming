#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 11:34:44 2021

@author: mansoor
"""

from do_something import *
import time
import multiprocessing

if __name__ == "__main__":
    start_time = time.time()
    size = 1000000
    procs = 10
    jobs = []
    for i in range(0, threads):
        out_list = list()
        process = multiprocessing.process(target=do_something,args=(size, out_list))
        jobs.append(process)
    for j in jobs:
        j.start()
        
    for j in jobs:
        j.join()
        
    print("List processing complete.")
    end_time = time.time()
    print("multiprocsses time=",end_time - start_time)