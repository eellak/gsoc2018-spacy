FILES=./*.html
for i in $FILES
do
    echo "awk '/^<li><span/ {print \$7;}' $i >> lemmas.out"
done


