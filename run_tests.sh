#!/bin/bash

# 1. Activate the virtual environment
# We check which folder exists to ensure it works on both Windows (Git Bash) and Linux (CI)
if [ -d "venv/Scripts" ]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

# 2. Execute the test suite using pytest
pytest

# 3. Return exit code 0 if passed, 1 if failed
# $? checks the exit code of the previous command (pytest)
if [ $? -eq 0 ]; then
    echo "Tests Passed!"
    exit 0
else
    echo "Tests Failed!"
    exit 1
fi