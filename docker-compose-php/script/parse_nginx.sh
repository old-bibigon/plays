#!/bin/bash
# сохранение списка уникальных ip с заходов в nginx в файл uniq_ips.txt

log_file="../logs/access.log"

cat "${log_file}" | cut -f 1 -d ' ' | sort | uniq -i > uniq_ips.txt
