# Bash autocomplete for pip

## Introduction

Herein the a Bash completion script for Python's pip command.

At
[Build Better Python Tools (Hackathon)](https://www.eventbrite.co.uk/e/building-better-python-tools-hackathon-tickets-14957023861),
2015-02-07, one table was looking at an update extension to pip. As part of this effort
[Charalampos (Harry) Papaloizou](https://github.com/papaloizouc) proposed creating a Bash completion script for pip
and this sub-project is the result -- aided and abetted by [Russel Winder](https://github.com/russel).

> Six hours to produce 5 lines of Bash script

However that was just the research and making a start, things have been and will continue to evolve.

## Installation

1. Clone this repository.
2. Copy or link the bash script ot he appropriate place.
3. Create the cache index of PyPI.
4. Use.

### Clone the repository

In a suitable directory:

```
$ git clone https://github.com/russel/pip_bashcompletion.git pip_bashcompletion
```

### Copy/link the Bash script

In the _auto\_complete_ subdirectory you will find the *pip* bash script and the index generator Python
script. You can either copy or symbolic link the bash script to install it. For global installation the
target directory is */etc/bash_completion.d*. For personal only installtion (more likely), the target directory
is *~/bash_completion.d*.

So for example, for a personal linked installation, assuming the Git repository is at
*/home/Git/pip_bashcompletion*:

```
$ cd ~/bash_completion.d
$ ln -s /home/Git/pip_bashcompletion/pip
```

### Create the cache indes of PyPI

PyPI has more than 55,000 packages so getting the list from PyPI for each completion action would definitely
be a ((very,) very,) very bad idea. Therefore the package list needs to be cached locally. This means iut
will need updating (manually for the moment, sorry) on a regular basis to ensure it is up-to-date. The
*pip_index_gen.py* script does all that is necessary to get the package list and output it to standard
output. To create, or update, the cache:

```
python pip_index_gen.py >> ~/.pip_index
```

### Use

No instruction should be needed for this phase. But remember to update the package cache from time to time.

## Current State

Completion is only undertaken on the install command.

Immediate next step deal with command completion.

## Licence

This work is licenced under the [MIT licence](http://opensource.org/licenses/MIT).
