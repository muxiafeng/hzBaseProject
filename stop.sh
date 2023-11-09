#!/bin/bash
ps -ef | grep app.py | awk '{print $2}' | xargs kill -9
