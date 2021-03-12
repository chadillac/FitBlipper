#!/usr/bin/env bash

dig axfr @b.root-servers.net . | grep NS | awk '{print $1}' | sort | uniq | cut -d'.' -f1 > tlds.txt
