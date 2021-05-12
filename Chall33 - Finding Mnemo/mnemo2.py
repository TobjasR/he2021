#!/usr/bin/python3

import binascii 
import hashlib
from mnemonic import Mnemonic


mnemo = Mnemonic("english")
words = "adapt bind bless blind civil craft garage good half hip home hotel lonely magnet metal mushroom napkin reason rescue ring shift small sunset tongue"
hextr = "3555 824e 8fcf 81db 03ec ed05 9db4 d2ba 1272 8d53 21b7 1cb0 e5b8 16b9 770e dd80 0829 ecd3 5ef2 e3b0 4ea1 f1f6 b271 f08d"
hashmap = dict(zip(hextr.split(' '), words.split(' ')))
w_array = [None] * 24

# it starts with half…
h = hashlib.sha256("half".encode("ascii")).hexdigest()
x = h[:4]
print("initial x (for half): " + x)

for i in range(24):
	for k in hashmap.keys():
		w = hashmap[k]
		h = hashlib.sha256(w.encode("ascii")).hexdigest()
		s = h[:4]
		if s == x:
			w_array[i] = w
			print(s + " -> " + w)
			x = k
			print("new x: " + k)
			break

wordz = " ".join(w_array)
print("wordz: " + wordz)
entropy = mnemo.to_entropy(wordz)
print("entropy: " + entropy.decode("ascii"))
	
"""
initial x (for half): a11a
a11a -> half
new x: 1272
1272 -> civil
new x: 03ec
03ec -> metal
new x: 770e
770e -> good
new x: d2ba
d2ba -> bless
new x: 8fcf
8fcf -> reason
new x: ecd3
ecd3 -> shift
new x: 4ea1
4ea1 -> home
new x: 21b7
21b7 -> garage
new x: 9db4
9db4 -> napkin
new x: 0829
0829 -> sunset
new x: b271
b271 -> tongue
new x: f08d
f08d -> bind
new x: 824e
824e -> rescue
new x: 5ef2
5ef2 -> mushroom
new x: dd80
dd80 -> hip
new x: 8d53
8d53 -> hotel
new x: 1cb0
1cb0 -> lonely
new x: e5b8
e5b8 -> blind
new x: 81db
81db -> small
new x: f1f6
f1f6 -> adapt
new x: 3555
3555 -> craft
new x: ed05
ed05 -> magnet
new x: 16b9
16b9 -> ring
new x: e3b0
wordz: half civil metal good bless reason shift home garage napkin sunset tongue bind rescue mushroom hip hotel lonely blind small adapt craft magnet ring
entropy: he2021{f1sh_r_fr1ends_n0t_f00d!}
"""