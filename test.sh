for f in $(ls *test.py | cut -d '.' -f1); do python2.7 -m unittest $f;done
