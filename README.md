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
````

## Author
Donald S Coon

donaldscoon@emailarizonaedu
