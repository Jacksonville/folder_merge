Folder Merge
============
##Introduction
This is a quick process that I wrote to merge photos taken on a couple of digital cameras into a single directory.

The idea was to use the date modified of the pictures to put the files into a chronicological sequence based on filename.

Where multiple files exist with the same date modified, a checksum appender is incrimented to ensure that no files are overwritten.

##Usage

usage: folder_merge.py [-h] source_path dest_path

A simple process to copy and rename files based on date modified. For example
a file named DCS_2342.jpg with a date modified of 2013-04-05 16:54:32 would be
renamed to 20130405_165432_0.jpg. If a file of the same name already exists in
the specified destination then the name would be 20130405_165432_1.jpg, the
last number incrimented until there is no conflict

positional arguments:
  source_path  Source path for copy
  dest_path    Destination path for copy

optional arguments:
  -h, --help   show this help message and exit

When source an destination paths are passed to this process the result is
files that are named in a similar manner