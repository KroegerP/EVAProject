#!/bin/bash

# If there's an error at the poetry --version, make sure that the pyenv installation was successfull and that
# the export text line got added to your bashrc file (nano ~/.bashrc to look)
poetry --version

echo 'The above line should produce something like "Poetry (X.X.X), currently 1.3.2 as of Jan 24th, 2023"'

echo "If there's an error at the poetry --version, make sure that the pyenv installation was successfull"

echo 'and that the export text line got added to your bashrc file "(nano ~/.bashrc to look)"'

poetry shell