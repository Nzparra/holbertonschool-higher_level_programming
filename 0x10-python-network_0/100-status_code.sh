#!/bin/bash
# request to a URL passed as an argument, and displays
curl -so /dev/null -w "%{http_code}" "$1"
