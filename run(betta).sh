echo Enter Name of accaunt:
read username
pyinstalive -d $username
sleep 3
cd ./Lives
python "./movement.py"
echo Done!
read -n 1 -r -s -p $'Press enter to continue...\n'