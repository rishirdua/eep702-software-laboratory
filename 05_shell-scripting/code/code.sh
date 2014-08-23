#take inputs from user
folder=$1
extension=$2

#check number of arguments
if [ $# != 2 ]
then
	echo Incorrect invocation
	echo USAGE
	echo code.sh foldername extensiontype
else
#run the code
	rm -f match.txt
	currentdir=`pwd`
	cd $folder
	#make list of folders
	list=`ls $folder | grep ^[a-z]*$`
	#make list of files
	for item in ${list//\\n/}
	do
		return=`find $item  -name "*.$extension"`
		if [ -z "$return" ]
		then
			a=10
		else
			#write to file
			echo "attempting to write"
			echo $item: >> 'match.txt'
			find $folder/$item  -name "*.$extension" >> 'match.txt'
		fi
	done
	echo done

	echo Executing files
	if [[ "$extension" == "sh" ]] #check extension
	then
		while read line
		do
			if [[ -n "$line" ]]
			then
				# do not process folder names
				if [[ ! "$line" =~ [a-z]*:$ ]]
				then
					name=${line##.*}
					temp=`bash $name`
					echo $temp
				fi
			fi
		done<match.txt
	fi
	if [[ "$extension" == "c" ]] #check extension
	then
		while read line
		do
			if [[ -n "$line" ]]
			then
				# do not process folder names
				if [[ ! "$line" =~ [a-z]*:$ ]]
				then
					name=${line##.*}
					temp=`gcc $name`
					echo $temp
					temp=`./a.out`
					echo $temp
				fi
			fi
		done<match.txt
	fi

	echo done
	# part b
	echo

	#replace caps by small alphabets
	for f in `find . -depth -type d`
	do
	   g=`dirname "$f"`/`basename "$f" | tr '[A-Z]' '[a-z]'`
	   if [ "xxx$f" != "xxx$g" ]; then
	      echo "Renaming folder $f"
	      mv -f "$f" "$g" 2>>log.txt
	   fi
	done

	#remove spaces
	find -name "* *" -type d | rename 's/ /_/g'

	#part c
	echo done
	echo
	echo "Checking for gif extension"

	if [[ "$extension" == "gif" ]] #check extension
	then
		while read line
		do
			if [[ -n "$line" ]]
			then
				# do not process folder names
				if [[ ! "$line" =~ [a-z]*:$ ]]
				then
					name=${line##.*}
					filename=${name%.gif}
					mv $line $filename.png 2>>log.txt #used when directory name and given argument are same
				fi
			fi
		done < match.txt
	else 
		echo Nothing to rename as your extension is not gif
	fi

	mv match.txt $currentdir/match.txt 2>>log.txt
fi
