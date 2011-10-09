#!/bin/sh

rsync --archive --force --delete --progress --compress --checksum --exclude-from=rsync_exclude.txt -e ssh ./ vjousse@jousse.org:flask/jousse/
