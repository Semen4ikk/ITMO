#!/bin/bash
export LANG=en_US.UTF-8
dir_count=0
file_count=0
count=0
function treee {
  local count=0
  if [ -d $dir/$1 ] && [ "$(ls $dir/$1)" ]; then
    dir_count=$(( dir_count + 1 ))
    local subdir=($dir/$1/*)
    dr=${subdir[@]##*/}
    parent=""
    for (( probeg=0;probeg<$2;probeg++ ));
    do parent="$parent\u2502\u00A0\u00A0\u0020"
      done
    child_dir=($dir/$1)
    if [ $3 == $4 ]; then
      printf "$parent\u2514\u2500\u2500 ${child_dir[@]##*/}\n"
      
      for i in ${dr[@]##*/}
      do count=$(( count + 1 ))
        treee "$1/$i" $(( $2 + 1 )) ${#subdir[@]} $count 1
        done
    else
      printf "$parent\u251c\u2500\u2500 ${child_dir[@]##*/}\n"
      for i in ${dr[@]##*/}
      do count=$(( count +1 ))
        treee "$1/$i" $(( $2 + 1 )) ${#subdir[@]} $count 0
        done
    fi
  else
    file_count=$(( file_count + 1 ))
    parent=""
    if [ $5 == 1 ]; then
      for (( probeg=0;probeg<$2-1;probeg++ ))
      do parent="$parent\u2502\u00A0\u00A0\u0020"
        done
      parent="$parent\u0020\u0020\u0020\u0020"
    else
      for (( probeg=0;probeg<$2;probeg++ ))
      do parent="$parent\u2502\u00A0\u00A0\u0020"
        done
    fi
    child_dir=($1)
    if [ $3 == $4 ]; then
      printf "$parent\u2514\u2500\u2500 ${child_dir[@]##*/}\n"
    else
      printf "$parent\u251c\u2500\u2500 ${child_dir[@]##*/}\n"
      
    fi
  fi
}
if [ -e $1 ] && [ $# -ne "0" ]; then
  dir=$1
else
  dir="."
fi
subdirs=($dir/*)

echo $dir

for i in ${subdirs[@]##*/}
do count=$(( count + 1 ))
  treee $i 0 ${#subirs[@]} $count 0
  done
direct=""
file=""
if [ $dir_count == 1 ]; then
  direct="directory"
else
  direct="directories"
fi
if [ file_count == 1 ]; then
  file="file"
else
  file="files"
fi
echo "$dir_count $direct, $file_count $file"
    
    

       
