for f in $(ls *test.py | cut -d '.' -f1); do ipython -m unittest $f;done
