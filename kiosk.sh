#!/bin/bash

function on_exit() {
	kill $pid
}

cd $(dirname $0)

trap on_exit EXIT

while true; do
	python ./src/main.py &

	pid=$!

	inotifywait -r -e modify --exclude '.*\.swp|.*\.pyc.*' ./src

	kill $pid
	wait $pid
done
