__author__ = 'Thygrrr'


import bsdiff4
import hashlib
import os
import sys
import shutil
import json

if __name__ == '__main__':
	source = sys.argv[1]
	target = sys.argv[2]
	patch  = "bsdiff4"

	if not os.path.exists(patch):
		os.makedirs(patch)

	for filename in os.listdir(target):
		source_file = os.path.join(source, filename)
		target_file = os.path.join(target, filename)

		source_data = open(source_file, "rb").read()
		target_data = open(target_file, "rb").read()

		if hashlib.md5(source_data).hexdigest() != hashlib.md5(target_data).hexdigest():
			print("diffing " + filename)
			patch_data = bsdiff4.diff(source_data, target_data)
			
			patch_file = os.path.join(patch, hashlib.md5(source_data).hexdigest())
			print("creating patch for " + filename + " with " + patch_file)
			open(patch_file, "wb+").write(patch_data)

		source_data = None
		target_data = None
		patch_data = None

	verify = {}
	for filename in os.listdir(target):
		filepath = os.path.join(target, filename)

		target_data = open(filepath, "rb").read()
		verify[filename] = hashlib.md5(target_data).hexdigest()

	with open("verify.json", "w+") as v:
		v.write(json.dumps(verify))

