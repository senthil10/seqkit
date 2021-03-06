#!/usr/bin/env python

import os
from glob import glob

def find_samples(proj_dir):
    """Find the samples in a given proj dir"""
    current_dir = os.getcwd()
    samples_fq = {}
    os.chdir(proj_dir)
    samples = [sam for sam in os.listdir(os.getcwd()) if os.path.isdir(sam)]
    for sam in samples:
        samples_fq[sam] = glob("{}/Rawdata/*.fastq*".format(sam))
    #    pdb.set_trace()
    os.chdir(current_dir)
    return samples_fq
