#!/bin/bash
while [1]
do
	if [ -f "telegram_details.json"]
	then
		python main.py
		echo "Panchanga dispatched  at $(date)"
		sleep $(($(date -f - +%s- <<< $'5 minustes\nnow')0))
	else
		echo "Telegram Details File not available in WorkDir"
	fi
done
