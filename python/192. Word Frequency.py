% (tr ' ' '\n' | sort | uniq -c | awk '{print $2"@"$1}') <<EOF

