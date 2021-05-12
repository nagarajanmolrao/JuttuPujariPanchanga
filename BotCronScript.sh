#!/bin/bash
while [ true ]
do
	if [ -f "telegram_details.json" ]
	then
		python main.py
		echo "Panchanga dispatched  at $(date)" >> /proc/1/fd/1
		sleep $(($(date -f - +%s- <<< $'tomorrow 04:30\nnow')0))
	else
		echo "Telegram Details File not available in WorkDir"
	fi
done
