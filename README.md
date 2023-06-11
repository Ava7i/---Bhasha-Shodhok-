

<a href="https://github.com/banglakit"><img src="https://avatars3.githubusercontent.com/u/20180620?s=125&amp;v=4" width="125" height="125" align="right" /></a>

# ভাষা-শোধক (Bhasha-Shodhok) 


| Version Info | [![Python](https://img.shields.io/badge/python-v3.9.0-blue)](https://www.python.org/downloads/release/python-3900/) [![Platform](https://img.shields.io/badge/Platforms-Ubuntu%2022.04.4%20LTS%2C%20win--64-orange)](https://releases.ubuntu.com/22.04/) [![RASA](https://img.shields.io/badge/RASA-v3.4.0-navy)](https://rasa.com/) |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |





<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Bangla, also known as Bengali, is an Indo-Aryan language spoken primarily in Bangladesh and the Indian state of West Bengal. The syntax or sentence structure of Bangla follows a subject-object-verb (SOV) format, which is common in many other languages of the Indian subcontinent.

A typical Bangla sentence consists of a subject, an object, and a verb. The subject is the person or thing performing the action described by the verb, while the object is the person or thing that the action is being performed on. The verb is the action word that describes the action being performed. In a simple sentence, the subject comes first, followed by the object and then the verb.

For example:

"আমি খাই (I eat)"

"আমি" (I) is the subject, "খাই" (eat) is the verb, and there is no object in this sentence.

In a compound sentence, the subject, object and verb can be separated by conjunctions. In a compound sentence, the subject and object can be separated by conjunctions like "এবং" (and) or "কিন্তু" (but).

For example:

"আমি খাই এবং স্নান করি (I eat and I bathe)"

"আমি" (I) is the subject, "খাই" (eat) is the verb and "স্নান করি" (I bathe) is the second clause of the sentence.

Bangla also has a rich vocabulary of particles and postpositions which are used to indicate the grammatical relationships between words in a sentence. These particles and postpositions can be used to indicate things like possession, direction, and time, among other things.

In addition, Bangla has rich conjugation system for verbs, nouns and adjectives. The conjugation system can express things like tense, mood, and number, among other things.

Overall, the syntax of Bangla language is rich and complex, but it is characterized by a SOV word order and rich conjugation system for verbs, nouns and adjectives, which makes it a fascinating language to learn.

Bengali and English are both languages, but they have different syntax or sentence structure. The main difference between Bengali and English syntax is the word order and the way they indicate grammatical relationships between words in a sentence.

Word order: Bengali is an SOV (Subject-Object-Verb) language, which means that the subject comes first, followed by the object and then the verb. On the other hand, English is an SVO (Subject-Verb-Object) language, which means that the subject comes first, followed by the verb and then the object.
Example:
Bengali: "আমি খাই (I eat)"
English: "I eat"

Particles and postpositions: Bengali has a rich vocabulary of particles and postpositions which are used to indicate the grammatical relationships between words in a sentence. These particles and postpositions can be used to indicate things like possession, direction, and time, among other things. On the other hand, English uses prepositions to indicate grammatical relationships between words in a sentence.
Example:
Bengali: "আমার কাছে বই (book in my place)"
English: "book in my place"

Conjugation system: Bengali has a rich conjugation system for verbs, nouns, and adjectives. The conjugation system can express things like tense, mood, and number, among other things. On the other hand, English has a simpler conjugation system and relies more on auxiliary verbs and word order to indicate tense and mood.
Example:
Bengali: "আমি খাই (I eat)"
English: "I eat"

Overall, the syntax of Bengali is different from that of English, but both languages can convey the same meaning through different sentence structure.







<!-- GETTING STARTED -->
## Getting Started

1. To get a local copy up and running follow these simple example steps.

```
mkdir venv
conda create -n venv python=3.9
conda activate venv
python3.9 -m venv ./venv
source ./venv/bin/activate
python3 -m pip install --upgrade pip
pip install --no-cache-dir -r requirements.txt


```
2.Then activate your venv 

```
 conda activate venv
```
3. After installing rasa we need to install spacy 
```
pip3 install rasa[spacy]
python3 -m spacy download en_core_web_md
<!-- en_core_web_md == 3.4.1 -->

```
4. After spacy, bangla bert should be installed
```
git lfs install
git clone https://huggingface.co/sagorsarker/bangla-bert-base
```
5. Then train the model

```
rasa train
```
6. you can Test the model 

``` 
rasa test nlu
```
7. There is also a shell prompt on rasa

```
rasa shell nlu
``
8. The results shows better in postman. If you need to enable the api , follow the below steps:
```
rasa run --enable-api --cors “*” --debug -p 8000
```


## Model naming conventions

In general, spaCy expects all model packages to follow the naming convention of
`[lang]_[name]`. For our models, we also chose to divide the name into three
components:

* **type**: Model capabilities (e.g. `core` for general-purpose model with vocabulary, syntax, entities and word vectors, or `depent` for only vocab, syntax and entities)
* **genre**: Type of text the model is trained on (e.g. `web` for web text, `news` for news text)
* **size**: Model size indicator (`sm`, `md` or `lg`)

For example, `en_depent_web_md` is a medium-sized English model trained on
written web text (blogs, news, comments), that includes vocabulary, syntax and
entities.

### Model versioning

Additionally, the model versioning reflects both the compatibility with spaCy,
as well as the major and minor model version. A model version `a.b.c`
translates to:

* `a`: **spaCy major version**. For example, `2` for spaCy v2.x.
* `b`: **Model major version.** Models with a different major version can't be loaded by the same code. For example, changing the width of the model, adding hidden layers or changing the activation changes the model major version.
* `c`: **Model minor version.** Same model structure, but different parameter values, e.g. from being trained on different data, for different numbers of iterations, etc.

For a detailed compatibility overview, see the [`compatibility.json`](compatibility.json).
This is also the source of spaCy's internal compatibility check, performed when you
run the `download` command.

## Downloading models

To increase transparency and make it easier to use spaCy with your own models,
all data is now available as direct downloads, organised in
[individual releases](https://github.com/banglakit/spacy-models/releases). spaCy
1.7 also supports installing and loading models as **Python packages**. You can
now choose how and where you want to keep the data files, and set up "shortcut
links" to load models by name from within spaCy. For more info on this, see the
new [models documentation](https://spacy.io/usage/models).

```bash
# pip install .tar.gz archive from path or URL
pip install /Users/you/bn_core_news_sm-2.0.0.tar.gz
pip install https://github.com/banglakit/spacy-models/releases/download/bn_core_news_sm-2.0.0/en_core_web_sm-2.0.0.tar.gz

# set up shortcut link to load installed package as "en_default"
python -m spacy link en_core_web_sm en_default

# set up shortcut link to load local model as "my_amazing_model"
python -m spacy link /Users/you/data my_amazing_model
```

## Loading and using models

`import` it directly and then call its `load()` method with no arguments.

> **⚠️ Important note:** Because the the Bangla models use a custom `SentenceSegmenter`,
> it is dynamically loaded with `model.load()`. Thus the sentence segmenter will
> not work if you load with `spacy.load('modelname')`.

```python
import spacy
import bn_core_news_sm

nlp = bn_core_news_sm.load()
doc = nlp(u'আমি বাংলায় গান গাই। তুমি কি গাও?')
```

## Manual download and installation

In some cases, you might prefer downloading the data manually, for example to
place it into a custom directory. You can download the model via your browser from
the [latest releases](https://github.com/banglakit/spacy-models/releases), or
configure your own download script using the URL of the archive file. The archive
consists of a model directory that contains another directory with the model data.

```yaml
└── bn_core_news_sm-2.0.0.tar.gz       # downloaded archive
    ├── meta.json                      # model meta data
    ├── setup.py                       # setup file for pip installation
    └── bn_core_news_sm                # model directory
        ├── __init__.py                # init for pip installation
        ├── meta.json                  # model meta data
        └── bn_core_news_sm-2.0.0      # model data
```

You can place the model data directory anywhere on your local file system. To
use it with spaCy, simply assign it a name by createing a shortcut link for the data directory.

**📖 For more info and examples, check out the [models documentation](https://spacy.io/usage/models).**


## Issues and bug reports

To report an issue with a model, please open an issue on the
[spaCy issue tracker](https://github.com/banglakit/spacy-models).
Please note that no model is perfect. Because models are statistical, their
expected behaviour **will always include some errors**. However, particular
errors can indicate deeper issues with the training feature extraction or
optimisation code. If you come across patterns in the model's performance that
seem suspicious, please do file a report.
