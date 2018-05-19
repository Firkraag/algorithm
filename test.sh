for f in $(ls *test.py | cut -d '.' -f1); do python3 -m unittest $f;done
