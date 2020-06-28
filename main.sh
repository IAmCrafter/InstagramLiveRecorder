while :
do
    source run.sh
    sleep 3
    cd ./Lives
    python "./movement.py"
    echo Done!
    cd ../
    # read -n 1 -r -s -p $'Press enter to continue...\n'
    sleep 1
    clear
done