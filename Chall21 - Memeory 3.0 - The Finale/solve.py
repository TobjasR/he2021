#!/usr/bin/env python3

import sys

# from scipy.misc.pilutil import imread
from matplotlib.pyplot import imread
from scipy.linalg import norm
from numpy import sum, average
from PIL import Image
import cv2
import json
import collections
import requests
import os
from lxml import html
from bs4 import BeautifulSoup

s = requests.Session()
url = "http://46.101.107.117:2107"
treshold = 31

# Main function, read two images, convert to grayscale, compare and print results:

def main():
	# first of all: download those cards (pictures)!
	dl_pics(url)
	# pics gonna be loaded in here:
	pics = {}
	# read images as 2D arrays (convert to grayscale for simplicity)
	print("converting to grayscale ...")
	for i in range(1, 99):
		pics[str(i)] = to_grayscale(imread(str(i)).astype(float))
		print(str(i), end=", ")
	# found pairs of card (pics) gonna go in there:
	pairs = {}
	print('\n' + "comparing pics and looking for pairs of cards ...", '\n' + "pairs = {", end='')
	# compare
	for i in range(1, 99):
		if str(i) not in pairs.keys() and str(i) not in pairs.values():
			for j in range(1, 99):
				if str(j) not in pairs.keys() and str(j) not in pairs.values():
					if i != j:
						img1  = pics[str(i)]
						img2  = pics[str(j)]
						if (img1.shape[0] == img2.shape[0] and img1.shape[1] == img2.shape[1]) or (img1.shape[0] == img2.shape[1] and img1.shape[1] == img2.shape[0]):
							if img1.shape[0] != img1.shape[1]:
								if i > j:
									i, j = j, i
								pairs[str(i)]=str(j)
								print('\"'+str(i)+ "\":\""+ str(j) + "\", ", end='')
								#print(str(i) + " " + str(j) + ": " + str(img1.shape[0]) + " " + str(img1.shape[1]) )
							else:
								if (mpp := compare_images(img1, img2) * 1.0 / img1.size) < treshold:
									pairs[str(i)]=str(j)
									print('\"'+str(i)+ "\":\""+ str(j) + "\", ", end='')
									#print(str(i) + " " + str(j) + ": " + str(mpp))
								elif (mpp := compare_images(img1, img2 = cv2.rotate(img2,cv2.ROTATE_90_CLOCKWISE)) * 1.0 / img1.size) < treshold :
									pairs[str(i)]=str(j)
									print('\"'+str(i)+ "\":\""+ str(j) + "\", ", end='')
									#print(str(i) + " " + str(j) + ": " + str(mpp))
								elif (mpp := compare_images(img1, img2 = cv2.rotate(img2,cv2.ROTATE_90_COUNTERCLOCKWISE)) * 1.0 / img1.size) < treshold :
									pairs[str(i)]=str(j)
									print('\"'+str(i)+ "\":\""+ str(j) + "\", ", end='')
									#print(str(i) + " " + str(j) + ": " + str(mpp))
								elif (mpp := compare_images(img1, img2 = cv2.rotate(img2,cv2.ROTATE_180)) * 1.0 / img1.size) < treshold :
									pairs[str(i)]=str(j)
									print('\"'+str(i)+ "\":\""+ str(j) + "\", ", end='')
									#print(str(i) + " " + str(j) + ": " + str(mpp))
	print("}")
	pairs_count = len(pairs)
	# if not all pair have been found, just give it up
	if pairs_count == 49 :
		print("###", str(pairs_count), "PAIRS FOUND! ###")
	else :
		print("!!! ONLY", str(pairs_count), "PAIRS FOUND !!!" + '\n' + " GIVING IT ANOTHER TRY ...")
		return
	# convert strings to integers
	pairs = {int(i):int(j) for i,j in pairs.items()}
	# send the solved pair to the web page
	send_solves(pairs)

# download pics

def dl_pics(url):
	print("loading page ...")
	r = s.get(url)
	# print("cookie: " + str(r.cookies))
	index_file = os.getcwd() + '/' + str(level) + ".txt"
	with open(index_file,'wb') as f : 
		f.write(r.content)
	# crawl the page
	soup = BeautifulSoup(r.content, "html.parser")
	#To find an element with a specific id:
	rcornersTotal = soup.find(id="rcornersTotal")
	if (not rcornersTotal) :
		print("No #rcornersTotal element found in page. EXITING ...")
		sys.exit()
	print("###", rcornersTotal.get_text(), "###")
	print("downloading pics ...")
	for i in range(1,99):
		r = s.get(url + "/pic/" + str(i), stream=True)
		if r.status_code == 200:
			filename = os.getcwd() + '/' + str(i)
			with open(filename, 'wb') as f:
				for chunk in r.iter_content(chunk_size=1024):
					if chunk:
						f.write(chunk)
				print(str(i), end=", ")
	print('\n' + "### pics downloaded! ###")

# If the file is a color image, imread returns a 3D array, average RGB channels (the last array axis) to obtain intensity. 
# No need to do it for grayscale images (e.g. .pgm):

def to_grayscale(arr):
	#"If arr is a color image (3D array), convert it to grayscale (2D array)."
	if len(arr.shape) == 3:
		return average(arr, -1)  # average over the last axis (color channels)
	else:
		return arr

# How to compare. img1 and img2 are 2D SciPy arrays here:

def compare_images(img1, img2):
	# normalize to compensate for exposure difference
	img1 = normalize(img1)
	img2 = normalize(img2)
	# calculate the difference and its norms (elementwise for scipy arrays)
	diff = img1 - img2
	# Manhattan norm
	m_norm = sum(abs(diff))
	# Zero norm
	# z_norm = norm(diff.ravel(), 0)
	return m_norm

# Normalization is trivial, you may choose to normalize to [0,1] instead of [0,255]. 
# arr is a SciPy array here, so all operations are element-wise:

def normalize(arr):
	rng = arr.max()-arr.min()
	amin = arr.min()
	return (arr-amin)*255/rng
	
# Send the solved pair to the web page

def send_solves(pairs):
	print("sending solves ...")
	for i,j in pairs.items():
		data = {"first":str(i), "second":str(j)}
		r = s.post(url + "/solve", data = data)
		if ("flag" in r.content.decode("utf-8")) :
			break
		else :
			print('\"' + r.content.decode("utf-8") + '\"', end=", ")
	if ("flag" in r.content.decode("utf-8")) :
		print('\n' + "### FINALLY, GOT DA FLAAAG!!1 ###", '\n')
		print('\"' + r.content.decode("utf-8") + '\"')
	else :
		print('\n' + "### solves sent! ###")
# Run the main function:

for i in range(1,21):
	global level
	level = i
	print('\n', "### " + str(i) + ". TRY ###")
	main()
	r = s.get(url)
	index_file = os.getcwd() + "/done.txt"
	with open(index_file,'wb') as f : 
		f.write(r.content)
