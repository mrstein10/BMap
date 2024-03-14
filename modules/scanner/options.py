#!/bin/bash

def showOptions(targets=""):
    print(targets)
    print("+----------------------------------------------------------------------+ \
    \n|                     |   Configuration   |                            | \
    \n|                     +-------------------+                            |")
    if targets != "":
        for host,port in targets:
            print(f"\n|     LHOST   {host}                                                     | \
        \n|     LPORTS  {port}                                                     |")
    else:
        print("\n|     LHOST   <none>                                                   | \
        \n|     LPORTS  <none>                                                   |")
    print("\n|                                                                      | \
    \n+----------------------------------------------------------------------+\n\n")

def showHelp():
    print("\n+----------------------------------------------------------------------+ \
    \n|                         |    Help    |                               | \
    \n|                         +------------+                               | \
    \n|                                                                      | \
    \n|      results  Show the results from the scan in a table.             | \
    \n|                                                                      | \
    \n+----------------------------------------------------------------------+\n\n")