cat purchases.txt | awk -F"    " '{print $6}' | sort | uniq -c
