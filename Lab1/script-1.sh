for file in *
do
if [ -f "$file" ] # check if file exists and is a regular file
then
i=0
while read -r line
do
i=$((i+1))
if (( i % 2 == 0 ))
then
echo "$file: $line"
fi
done < "$file"
fi
done
