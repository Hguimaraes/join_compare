#!/bin/bash
rm lefttable_ordered.txt lefttable_unordered.txt righttable_ordered.txt righttable_unordered.txt
python generator.py
python join_compare.py
