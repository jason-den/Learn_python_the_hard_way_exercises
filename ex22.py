# More Files
from sys import argv
from os.path import exists  # tasets good.


script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do thses two on one line, how?
#in_data = (open(from_file)).read()  # after sucsess, unwrap the ()
in_file = open(from_file)
in_data = in_file.read()

print "The input file is %d bytes long." % len(in_data)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
# when we write a file, we '>' it, not '>>'. so, it would clean
# anything inside of the original file. 
out_file.write(in_data)



print "Alright, all done."

out_file.close()
in_file.close()

     