#!/usr/bin/env python

import os
import pwd
import argparse
import subprocess
import time

#commands that are alloed
parser = argparse.ArgumentParser(description='always')
parser.add_argument("--sleep", dest="sleep", default=100.0, help="how long to sleep between restarts")
parser.add_argument("--retries", dest="retries", default=5, help="how many times to retry before giving up")
parser.add_argument("--warmup", dest="warmup", default=5, help="min time program has to run before failed attempt")
parser.add_argument("--fork", dest="fork", action="store_true", help="Not working yet")
parser.add_argument("--user", dest="user", help="set the user to run command as")
parser.add_argument("--uid", dest="uid", help="set uid of user to run command ad")
parser.add_argument("--", "--cmd", dest="cmd", help="command with flags that you wish to run")
args = vars(parser.parse_args())

#get the user id of a user we wish to switch to
if args.get('user'):
    try:
        args['uid'] = pwd.getpwnam(args.get('user')).pw_uid
    except:
        print "Failed to get uid of {0}".format(args.get('user'))
        exit()

#lets switch to a differnet user
if args.get('uid'):
    os.setuid(args.get('uid'))

#set the attempts made to 0 for starters
attempts = 0

if type(args.get('cmd')) is str:
    while True and attempts < int(args.get('retries')):
        attempts += 1 #set attempts up by 1
        start_time = time.time() #set start tiume
        
        proc = subprocess.Popen([args.get('cmd')], shell=True) #run the command we wish to run
        proc.wait() #lets just sit and wait until we have more info
        
        #if we have been up long enough to been running lets set attempts to 0
        if time.time()-start_time > int(args.get('warmup')):
            attempts = 0
        
        time.sleep(float(args.get('sleep', 100.0))/1000.0) #sleep for a little bit so we dont kill our sleves

