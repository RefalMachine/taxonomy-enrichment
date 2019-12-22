# taxonomy-enrichment
Useful materials for participants of the Dialogue 2020 shared task on taxonomy enrichment

#### Link to competion: [codalab](https://competitions.codalab.org/competitions/22168)
#### Link to discussion group: [Telegram](https://t.me/joinchat/Ckja7Vh00qPOU887pLonqQ)

#### Evaluation script:
```
usage: evaluate.py [-h] [--mixed] full direct predicted

positional arguments:
  full
  direct
  predicted

optional arguments:
  -h, --help  show this help message and exit
  --mixed
```
If --mixed is used full must be in next format:
word_1 hypernym_1 hypernym_1_1 hypernym_1_2
word_2 hypernym_2 hypernym_2_1
...

#### Links to additional data:

* [News corpus](http://bit.ly/38CLlmW)
* [Hypernym database](http://panchenko.me/data/joint/isas/ru-librusec-wiki-diff.csv.gz)
* [Parsed Russian Wikipedia](http://panchenko.me/data/joint/corpora/wikipedia-ru-2018.txt.gz)
* [Additional text corpus](http://panchenko.me/data/russe/librusec_fb2.plain.gz)
