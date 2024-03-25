#!/bin/bash
pip_list="$(pip list)"
# shellcheck disable=SC1089
if! echo "$pip_list" | grep -q "request"; then
    pip install -r requirement.txt
fi

nohup python3 /pythonProject/hzBaseProject/app.py > /pythonProject/hzBaseProject/baseProject.log 2>&1 &
