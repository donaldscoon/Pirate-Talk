Pirate-Talk
===========
## Description
Recreation of an infamous insult competition between two scallywags. Output one insult at a time with 5 seconds between each insult. Featuring Cantankerous Tim and Black Spot Pete.

Accepts -r (--rounds) as an argument that sets the number of rounds the insults go back and forth.

Inspiration: https://www.youtube.com/watch?v=SLrUpiePR60

## How to run the program
````
usage: pirate_talk.py [-h] -r int

Argparse Python script

optional arguments:
  -h, --help            show this help message and exit
  -r int, --rounds int  Number of rounds in the insult competition
````
## Expected output
````
$ python3 pirate_talk.py -r 2
Cantankerous Tim says: My fresh born lass swears better you, yer a pin-headed, barnacle-backed, peice-of-filth!!!

 Black Spot Pete says: You're a cricket-sized, cross-eyed, whale-fart!!!
````
     
## Description of how to run the tests.
````
$ make test
python3 -m pytest -v test.py
============================================================================== test session starts==============================================================================
platform linux -- Python 3.6.7, pytest-4.3.0, py-1.8.0, pluggy-0.9.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /mnt/c/Users/Donald/Pirate-Talk, inifile:
collected 2 items                                                                                                                                                               

test.py::test_usage PASSED                                                                                                                                                [ 50%]
test.py::test_play11 PASSED                                                                                                                                               [100%]

=========================================================================== 2 passed in 20.53 seconds===========================================================================
````

## Author
Donald S Coon

donaldscoon@emailarizonaedu
