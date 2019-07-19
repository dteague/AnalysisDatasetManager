#!/usr/bin/env python

import argparse
import glob
import os
import subprocess
import multiprocessing

parser = argparse.ArgumentParser()
parser.add_argument("path", type=str, help="path to files in hdfs")
parser.add_argument("-a", "--storage_area", type=str, default="data",
        help="Are to store files (default /data)")
parser.add_argument("-s", "--selection", type=str, default="Dilepton",
        help="Selection tier (default Dilepton)")
parser.add_argument("-d", "--data_name", type=str, default="DibosonAnalysisData",
        help="Data name")
parser.add_argument("-u", "--username", type=str, default="%s" % os.getlogin(),
        help="Username for storage area, default is your login username")
parser.add_argument("--hadd", action='store_true',
        help="Combine files with hadd")
args = parser.parse_args()

if "store" in args.path[:7]:
    args.path = "/hdfs" + args.path
for directory in glob.glob(args.path):
    print "Copying directory", directory
    if not os.path.isdir(directory):
        print "Invalid filename: %s" % directory
        exit(1)
    dirs = directory.split("/")
    dir_name = dirs[-1]
    if dir_name[:3] == "000" and len(dirs)>= 5:
        if "/hdfs" in directory:
            indices = (6,8)
        else:
            indices = (5,7)
        dir_name = dirs[indices[0]]
        if any(y in dir_name for y in ["Muon", "EG", "Electron"]):
            dir_name = "_".join(dirs[indices[0]:indices[1]])
    new_dir = "/".join(["/data", args.username, args.data_name, args.selection.strip("/"), dir_name])
    if "eos" in args.storage_area:
        new_dir = "/".join(["/eos/user", args.username[0], args.username, args.selection, dir_name])
    elif "nfs_scratch" in args.storage_area:
        new_dir = new_dir.replace("data", "nfs_scratch")
    try:
        os.makedirs(new_dir)
    except OSError as e:
        print e
        continue
    filenames = [f if "hdfs" not in f else f[5:] for f in glob.glob(directory + "/*.root")]
    if len(filenames) == 0:
        print "WARNING: No files found for directory %s. Skipping." % directory
        continue
    p = multiprocessing.Pool(processes=10)
    p.map(subprocess.call, [["xrdcp", 
            "root://cmsxrootd.hep.wisc.edu/%s" % filename, 
            new_dir] for filename in filenames]
        )
    if args.hadd:
        subprocess.call(["hadd", "%s/combined.root" % new_dir] + glob.glob("%s/*.root" % new_dir))
