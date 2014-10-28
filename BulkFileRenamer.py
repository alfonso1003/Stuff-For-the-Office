#!/usr/bin/env python
 
# os is a library that gives us the ability to make OS changes
# re is a libary for working with regular expressions
# sys is a library to interact with the system, e.g. commandline arguments.
# credit goes to for source code: http://pastebin.com/6NF8MPcF
import os
import re
import sys
 
 
def get_files(directory):
    retval = {}
    files = os.listdir(directory)
    expr = re.compile(r'^\d+')
    # holds the max witdh necessary for representing all prefixes
    max_width = 0
    # iterate over every file name in the directory
    for file_name in files:
        match = re.match(expr, file_name)
        if not match:
            print "Skipping %s: it doesn't start with a number." % (file_name, )
            continue
        file_number = int(match.group())
        file_remainder = file_name[match.end():]
        # Corner cases such as starting with 99: next number is 100, which is wider.
        max_width = max(max_width, len(str(file_number + 1)))
        # Makes it easier to properly sort in increment_file_numbers()
        retval.update({file_number: (file_name, file_remainder)})
    return((max_width, retval))
 
 
def increment_file_numbers(directory, number, width=0):
    max_width, files = get_files(directory)
    # Ensure that all numbers get an equal width, even if a lower width was
    # passed on the command line.
    width = max(width, max_width)
    # Sort high to low, numerically
    file_numbers = sorted(files.keys(), reverse=True)
    for file_number in file_numbers:
        # we only increment the files that are bigger than number
        if file_number >= number:
            new_file_number = file_number + 1
        else:
            new_file_number = file_number
 
        # use string formatting to pad narrower nums with zeroes
        prefix = '{0:0{1}}'.format(new_file_number, width)
        new_file_name = os.path.join(directory,
            prefix + '%s' % (files.get(file_number)[1], ))
        old_file_name = os.path.join(directory, files.get(file_number)[0])
 
        # Don't rename files if their name is unchanged. Allows for renaming
        # when width of prefix changes.
        if new_file_name == old_file_name:
            continue
        # rename the file!
        if not os.path.basename(new_file_name) in os.listdir(directory):
            print '%s ==> %s' % (os.path.basename(old_file_name),
                os.path.basename(new_file_name))
            os.rename(old_file_name, new_file_name)
        else:
            # Can't really happen, unless a rename went wrong, as we're
            # renaming from high to low and skipping renames to self.
            print "Skipping rename of %s because new filename %s already exists." % \
                (os.path.basename(old_file_name), os.path.basename(new_file_name))
 
 
if __name__ == '__main__':
    if len(sys.argv) >= 2:
        path = os.getcwd()
        number = int(sys.argv[1])
        if len(sys.argv) == 3:
            width = int(sys.argv[2])
        else:
            width = 0
        increment_file_numbers(path, number, width)
    else:
        print "Usage: %s <nbr> [width]\n"  % (sys.argv[0], ) + \
            "Where nbr is the first number you wish to increment,\n" + \
            "and width is the number of digits used for the numbering."
