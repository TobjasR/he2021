#!/usr/bin/env python

import hashlib

name = "COLA DECAF"
key1 = "c01a"
key2 = "decaf"

for i in range(10000000, 99999999):
	s = str(i) + " " + name
	hash = "" + hashlib.sha256(s.encode("utf-8")).hexdigest()
	if key2 in hash:
		print(s)
		print(hash)
		break