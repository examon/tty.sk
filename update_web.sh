#!/bin/bash

./make_list.py database.links web/stuff.html
scp web/* tty.sk@tty.sk:/web
