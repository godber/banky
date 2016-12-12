# Banky - Exam Generation Tool and Test Bank.

Banky is comprised of the following components:

* **Test Bank** - A directory hierarchy that stores all questions one of the
  supported plain text question formats.
* **Question Selection Tool** - A tool that helps users select questions from
  the Test Bank to create an exam.
* **Exam Builder** - generates a LaTex version of an exam.

## Test Bank

The **Test Bank** can be found under the `test_bank/` directory and contains
all of the questions.  Each question must have it's own directory and that
directory should contain the following things:

* **Index File** - The index file is main file that stores the question.  It can
  be a MarkDown, LaTex, or YAML file.  It must be named `index.md`, `index.tex`,
  or `index.yml`.  Each question directory must contain only ONE `index.*` file.
* **Meta File** - The metafile is named `meta.yml` and contains any
  meta-information related to the question.  This will include `tags` that will
  help query the questions and possibly `course` and `semester` information.
* **Support files** - (Optional) - Any code or image files that are included or
  required by the index file.
* **Answer File** - (Optional) - TBD, for grading keys
* **Raw Files** - (Optional) - Original raw text extract

With the exception of the single question per directory requirement, the user
may use any directory structure they choose to.  The directory names will be
incorporated into a `dir_tag` list that can be queried against so users can use
the directory structure to guide queries.  So for instance a directory named
`ecn315/trade/hawley_smoot/q1/` will have:

```
dir_tags = ['ecn315', 'trade', 'hawley_smoot']
```

Note that `q1` is omitted.  The dirname `qN` where `N` is a positive integer
is assumed to just be a question identifier, so this magic value is omitted
from the `dir_tags` list.

**NOTE**: The question terminal directory names will need to be unique when
copied into the exam directory.  So we either need to enforce that uniqueness
here or copy the directory structure or consolidate the parent directory names
into one directory name in the exam dir.

### Tools

* `banky q new <dir_name>` - Creates directory and empty `index.*` and
  `meta.yml` files.
* `banky check` - Validates that all directories satisfy the requirements.

It is assumed that you run the banky command somewhere under your banky topdir.
The topdir should contain a `.banky.conf` file, `test_bank/` and `tests/`
directories.

### Index Files

Explain in more detail what they must/may contain.

### Meta Files

I am not sure what these really need to be, I want to depend on tags as much as
possible but it might be important to store certain information explicitly, like
course, creation date, etc.

## Exam Builder

Each exam must be a directory stored as a subdirectory of the `exams/`
directory.  Questions in exams are just like those in the `test_bank`, they
are directories containing those items listed above.  Typically they are copied
from the `test_bank` using the **Question Selection Tool**.

`banky exam` - shows lists of exams
`banky exam new [exam_name]` - creates exam directory

Generating and building the exam (run in exam dir):

`banky exam generate` - generates the consolidated exam source file in the
desired output (MarkDown, LaTex) in the `src/` directory.
`banky exam build` - generates the final output files from all exams found in
the `src/` directory.  These output files are typically HTML or PDF and will be
placed in the `builds/` directory.

Questions/Ideas:

* The generate step is where we can do question randomization.
* Maybe we can create question groups using subdirectories.
* We can use an exam manifest YAML file to specify specific orderings
  of questions.  This could be generated with a tool using the exam
  subdirectory.  This could possibly address the need for groupings and other
  exam header information.  For example:

```yaml
Exam 2 for Econ 315:
  - meta:
    - date: 12/07/2016
    - instructions: "Fill in the bubbles in the Scantron."
    - page_numbers: False
    - generate_key: True
  - Banks:
    - meta:
      - randomize_questions: True
      - randomize_options: True
    - bankq1
    - bankq7
    - bankq9
  - Trade:
    - tradeq9
    - importq2
```

## Question Selection Tool

This is a query tool that allows you to select questions from the `test_bank/`
directory that match a specified criteria.

`banky q <string>` - search for string in `tags`, `dir_tags`

More complicated queries might be made available in the future.

Not sure.
