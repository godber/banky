This should work in Python 3 and be fairly easy to get up and going.

```bash
mkvirtualenv -p `which python3` gfaq
pip install -U pip
pip install -r requirements3.txt
```

Now you can validate the sample question:

```bash
./validate.py question-b.yml
```

Try screwing up the sample file, `question-b.yml`, and running the validator on
it again.

Now try and generate the OLX (EdX XML Question Format) from the sample file,
`question-b.yml`:

```bash
./gen.py question-b.yml
cat question-b.xml
```
