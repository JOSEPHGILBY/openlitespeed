#!/bin/sh

url=$1
dest_path=$2
max_attempts=5
attempt_num=1

while [ $attempt_num -le $max_attempts ]
do
    echo "Attempt #$attempt_num to clone $url into $dest_path..."
    git clone "$url" "$dest_path" && break
    attempt_num=$((attempt_num+1))
    sleep 5
done

if [ $attempt_num -gt $max_attempts ]; then
    echo "Failed to clone $url after $max_attempts attempts."
    exit 1
fi

echo "Successfully cloned $url into $dest_path."
exit 0