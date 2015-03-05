# always
Make sure commands keeps running always

Simualir too [forever](https://github.com/foreverjs/forever) but written in python. Simpler then [Supervisor](http://supervisord.org/) or [Circus](http://circus.readthedocs.org/en/0.11.1/) because its made to be adhoc and no config file requried. 

##10 Second how to

```
python always.py --cmd "date"
Wed Mar  4 17:38:45 PST 2015
Wed Mar  4 17:38:45 PST 2015
Wed Mar  4 17:38:45 PST 2015
Wed Mar  4 17:38:45 PST 2015
Wed Mar  4 17:38:45 PST 2015
```

Alaways will restart a command that fails. and will keep running it up to how many retries and a few other things

```
$ ./always.py -h
usage: always.py [-h] [--sleep SLEEP] [--retries RETRIES] [--warmup WARMUP]
                 [--fork] [--user USER] [--uid UID] [-- CMD]

always

optional arguments:
  -h, --help         show this help message and exit
  --sleep SLEEP      how long to sleep between restarts
  --retries RETRIES  how many times to retry before giving up
  --warmup WARMUP    min time program has to run before failed attempt
  --fork             Not working yet
  --user USER        set the user to run command as
  --uid UID          set uid of user to run command ad
  -- CMD, --cmd CMD  command with flags that you wish to run
  ```

##Author

Alexis Okuwa - [wojons](https://github.com/wojon)

##Todo
 - Setup.py and upload to Pypi For it to be useful
 - The fork freature is currently not  set up at this time to work.
