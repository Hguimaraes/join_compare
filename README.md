# join_compare

This repository was created as part of the Database Construction Course @ UFRJ by group E (Heitor Guimarães, Igor Amaral, Vinícius Almeida)

To run the code, first run the **generator.py** script passing the number of lines desired as an argument:

	$ python generator.py "numberoflines"

The generator script generates four files:

* left_ordered.txt
* left_unordered.txt
* right_ordered.txt
* right_unordered.txt

with the following format:
	
	Left files: pkey, value
	Right files: pkey, fkey, value

after running the generator script, install the **BTree.OBBTree** module by running:

	$ pip install BTrees

after that, you may run the **join_compare.py** file by running:

	$ python join_compare.py

for this directed study, the following datasets size were used: 10000, 100000 and 1000000 lines.
The results are the following:

| Dataset Size | Ordered Nested Loop | Unordered Nested Loop | Merge-Join | Hash Join | BTree Join |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 10000 | 19.96sec | 19.25sec | 0.03sec | 0.02 sec | 0.04sec |
| 100000 | N/A | N/A | 0.28sec | 0.26sec | 0.54sec |
| 1000000 | N/A | N/A | 2.76sec | 2.75sec | 7.68sec |
