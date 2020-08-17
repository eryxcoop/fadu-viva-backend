#!/usr/bin/env bash
echo "Updating status"
wget -O/dev/null -nv -S http://fadubackend:5000/api/update-traffic-status
wget -O/dev/null -nv -S http://fadubackend:5000/api/update-buses-gps
