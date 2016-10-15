#!/usr/local/bin/zsh
export PATH="/usr/local/bin:/usr/local/sbin:/usr/bin:/bin:/usr/sbin:/sbin"
PATH=$PATH:/Users/C/.shell

function stopserver(){
	echo "to kill server process"
	ps aux | grep jekyll| while  read DL
	do
		eval $(echo $DL | awk -F " " '{print "tmp="$2 ; }' );
	    if [ $tmp -lt $$ ]; then
	    	echo "杀死 pid = $tmp "
	    	kill -9 $tmp
	    fi
	done
}

function commitpush(){
    git checkout source
    echo "to push source"
	/usr/local/bin/jekyll build

	mv _site ..
	rm -rf .sass-cache

	git add -A
	git commit -m "update source"


	git checkout master
	echo "to push master"
	rm -rf ./*
	mv ../_site/* .
	rm -rf .sass-cache
	rm -rf ../_site

	git add -A
	git commit -m "deploy blog"
	    
	git checkout source
}
function startserver(){
	/usr/local/bin/jekyll serve --host 0.0.0.0 --port 5001 --watch  1>/dev/null &
} 
function prexe(){
	# $(which python3) /Users/C/.shell/seal
	# $(which python)  /Users/C/.shell/addtime
} 
function helpinfo(){
	echo "----------------------------------------------------------------------"   
	echo "  ./run.sh p l k     "
	echo "----------------------------------------------------------------------"
}




if [[ $# == 0 ]]; then
	helpinfo
elif [[ $1 == "l" ]]; then    
	stopserver;
	prexe;
	git checkout source
	/usr/local/bin/jekyll build;
	startserver;
elif [[ $1 == "p" ]]; then
	stopserver;
	prexe;
	commitpush;
elif [[ $1 == "k" ]]; then
	stopserver;
elif [[ $1 == "pl" ]]; then
	stopserver; 
	prexe;
	commitpush;
	git checkout source
	/usr/local/bin/jekyll build;
	startserver;
fi