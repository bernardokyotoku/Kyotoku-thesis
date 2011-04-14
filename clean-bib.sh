#!/bin/bash

cat $1 | sed -E 's/^(uri|local-url|URL|abstract).*//' > clean-$1
