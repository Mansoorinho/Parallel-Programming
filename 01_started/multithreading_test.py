#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 11:14:46 2021

@author: mansoor
"""

from do_something import *
import time
import threading

if __name__ == "__main__":
    start_time = time.time()
    size = 1000000
    threads = 10
    jobs = []
    for i in range(0, threads):
        out_list = list()
        thread = threading.Thread(target=list_append(size, out_list))
        jobs.append(thread)
        
        for j in jobs:
            j.start()
        for j in jobs:
            j.join()
            
        print("List processing complete.")
        end_time = time.time()
        print("multithreading time =", end_time - start_time)