#!/usr/bin/env python
import csv
import numpy as np
from argparse import ArgumentParser

def read_data(fname):
	return np.genfromtxt(fname, delimiter=',')

def avg_col(data):
	return np.mean(data, axis=0)

def write_data(fname,data):
	np.savetxt(fname, data, delimiter=',', fmt='%d')


if __name__ == "__main__":
	parser = ArgumentParser(description="Access csv data file")
	parser.add_argument('--ifile','-i')
	parser.add_argument('--ofile','-o')
	arguments = parser.parse_args()

	data = read_data(arguments.ifile)
	avg = avg_col(data)
	write_data(arguments.ofile,avg)
