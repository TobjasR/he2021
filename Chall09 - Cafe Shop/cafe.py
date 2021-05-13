#!/usr/bin/env python

import hashlib

name = "COLA DECAF"
c01a = "c01a"
decaf = "decaf"

for i in range(10000000, 99999999):
	id_string = str(i) + " " + name
	id_hash = hashlib.sha256(id_string.encode()).hexdigest()
	if c01a in id_hash and decaf in id_hash:
		print("id_string: " + id_string)
		print("id_hash: " + id_hash)
		break

# eventually hits at 37374099 (37%) and outputs:
# id_string: 37374099 COLA DECAF
# id_hash: f5ba3332710abaf7d01decaff966e3e6cc579a5274f8be9cf3442d3c01a373fb
