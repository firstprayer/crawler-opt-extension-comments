# crawler-opt-extension-comments
This is a crawler for all comments on [public comment page for OPT Extension](http://www.regulations.gov/#!docketBrowser;rpp=25;so=DESC;sb=postedDate;po=50;dct=PS;D=ICEB-2015-0002;refD=ICEB-2015-0002-0011). 

# Usage
Just do:
    sudo make install
    make run

All the comments will store in the comments.txt. Each line is one comment. The comments are sorted by time from oldest to newest.

# Suggestions
[gensim](https://radimrehurek.com/gensim/index.html): Topic modeling
[sklearn](http://scikit-learn.org/stable/): Classifier training


