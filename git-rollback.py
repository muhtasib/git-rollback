#!/usr/bin/python

#This command rolls back commits
# Option -k or --keep, keeps files staged, default is no
# Option -w or --wipe, wipes files from a rollback all together, default is no

import sys, os

def localRollback(opts):
  keep = 'no'
  wipe = 'no'
  
  for o in opts:
    if o in ("--keep", "-k"):
      keep = 'yes'
    if o in ("--wipe", "-w"):
      wipe = 'yes'
  
  if keep == 'yes' and wipe == 'yes':
    print 'Wipe will not keep any files to be staged. Ignoring keep.'

  print "You are rolling back your local commit."

  if wipe == 'yes':
    os.system('git reset --hard HEAD^');
  else:
   os.system('git reset --soft HEAD^;');
   if keep == 'no':
     os.system('git reset');

def remoteRollback():
  print "You are rolling back your remote commit. Not implemented yet."
 
def main():
  if len(sys.argv) < 2:
    print 'Please specify a command.'
    usage()

  first_arg = sys.argv[1]
  
  if first_arg == "local":
    localRollback(sys.argv[2:])
  elif first_arg == "remote":
    remoteRollback()
  elif first_arg == "--help" or first_arg == "-h":
    usage()
    
def usage():   
    print ' ---------------------------------------------------------------------------------------------'
    print ' Leila Muhtasib, June 5, 2012'
    print ' '
    print ' This command rolls back your last commit. '
    print ' '
    print ' Typical usage:'
    print ' git rollback local'
    print ' '
    print ' SYNOPSIS: git rollback <command> [<args>]'
    print ' '
    print ' Commands:'
    print ' local   Rollback a local commit.'
    print ' remote  Rollback a commit made to the server.'
    print ' '
    print ' Options (only for local command):'
    print ' --keep or -k  Keep files you have just unrolled in the staging area.'
    print ' --wipe or -w  Wipes out your changes and gives you a clean working area after you rollback.'
    print ' You either keep or wipe the files. You cannot do both.'
    print ' ---------------------------------------------------------------------------------------------'
    sys.exit(' ')

#----------------------------------------------
    
if __name__ == "__main__":
  main()
