---
date: "2023-09-26"
title: "Awk Sed bash"
---
<!-- markdownlint-disable MD025 -->
# Awk Sed
<!-- markdownlint-enable MD025 -->

## Introduction

Don't forget to use both `man` and `info` commands to learn more about the vairous utitlies that `sed` and `awk` depend upon, like `sort`, `xargs` and `find` for example.

## sed

* [Sed - grymoire - An Introduction and Tutorial by Bruce Barnett](https://www.grymoire.com/Unix/Sed.html)
* [Sed Cheat Sheet](https://catonmat.net/ftp/sed.stream.editor.cheat.sheet.txt)
* [sed . . . the stream editor](https://www.pement.org/sed/index.htm)
* [sed single page manual](https://www.gnu.org/software/sed/manual/sed.html)

## bash

* [bash manual](https://www.gnu.org/software/bash/manual/bash.html)
* [bash debugger](https://bashdb.sourceforge.net/bashdb.html)
* [debugging bash scripts](https://linuxconfig.org/how-to-debug-bash-scripts)

## Here documents

[Here Documents](https://tldp.org/LDP/abs/html/here-docs.html)

```bash
#!/bin/bash
# generate-script.sh
# Based on an idea by Albert Reiner.

OUTFILE=generated.sh         # Name of the file to generate.

# -----------------------------------------------------------
# 'Here document containing the body of the generated script.
(
cat <<'EOF'
#!/bin/bash

echo "This is a generated shell script."
#  Note that since we are inside a subshell,
#+ we can't access variables in the "outside" script.

echo "Generated file will be named: $OUTFILE"
#  Above line will not work as normally expected
#+ because parameter expansion has been disabled.
#  Instead, the result is literal output.

a=7
b=3

let "c = $a * $b"
echo "c = $c"

exit 0
EOF
) > $OUTFILE
# -----------------------------------------------------------

#  Quoting the 'limit string' prevents variable expansion
#+ within the body of the above 'here document.'
#  This permits outputting literal strings in the output file.

if [ -f "$OUTFILE" ]
then
  chmod 755 $OUTFILE
  # Make the generated file executable.
else
  echo "Problem in creating file: \"$OUTFILE\""
fi

#  This method also works for generating
#+ C programs, Perl programs, Python programs, Makefiles,
#+ and the like.

exit 0
```

```bash
#!/bin/bash
# here-function.sh

GetPersonalData ()
{
  read firstname
  read lastname
  read address
  read city 
  read state 
  read zipcode
} # This certainly appears to be an interactive function, but . . .

# Supply input to the above function.
GetPersonalData <<RECORD001
Bozo
Bozeman
2726 Nondescript Dr.
Bozeman
MT
21226
RECORD001

echo
echo "$firstname $lastname"
echo "$address"
echo "$city, $state $zipcode"
echo

exit 0
```

## awk

```bash
awk -f awkscriptfile

cat << "EOF" > executableawk
#!/bin/awk -f
BEGIN {
    lines=0;
    total=0;
}
{
# increase the number of files
    lines++;
# increase the total size, which is field #1
    total+=$1;
}
END {
    print lines " lines read";
    print "total is ", total;
    if (lines > 0 ) {
        print "average is ", total/lines;
    } else {
        print "average is 0";
    }
}
EOF
chmod +x executableawk
wc -c * | ./executableawk

# ${variable:-defaultvalue}, variable=value
cat << "EOF" > bashawk.sh
#!/bin/sh
awk '{print $c}' c="${1:-1}"
# awk '{print $'"${1:-1}"'}'
# or 
# column="${1:-1}"
# awk '{print $'"$column"'}'
EOF
chmod +x bashawk.sh
ls -l | ./bashawk.sh 9 # filename printed
```

awk command summary:

```awk
~ # matches
!~ # doesn't match
&& || # and or
if ( conditional ) statement [ else statement ]
while ( conditional ) statement
for ( expression ; conditional ; expression ) statement
for ( variable in array ) statement
break
continue
{ [ statement ] ...}
variable=expression
print [ expression-list ] [ > expression ]
printf format [ , expression-list ] [ > expression ]
next
exit
```

* [GAWK: Effective AWK Programming, single page manual](https://www.gnu.org/software/gawk/manual/gawk.html)
* [Awk, Nawk and GNU Awk Cheat Sheet](https://catonmat.net/ftp/awk.cheat.sheet.txt)
* [Awk One-Liners Explained, Part I: File Spacing, Numbering and Calculations](https://catonmat.net/awk-one-liners-explained-part-one)
* [Awk One-Liners Explained, Part II: Text Conversion and Substitution](https://catonmat.net/awk-one-liners-explained-part-two)
* [Awk One-Liners Explained, Part III: Selective Printing and Deleting of Certain Lines](https://catonmat.net/awk-one-liners-explained-part-three)
* [awk - grymoire - An Introduction and Tutorial by Bruce Barnett](https://www.grymoire.com/Unix/Awk.html) it's worth noting that grymoire's notes are for very old versions of Unix and Linux. For the example of `count_new_users` the sort that I used was `sort -k 1nr,2 -k 3d,4` and not the, by today's standards, cryptic original `sort +0nr -2 +2d`
* [awk is a beautiful tool](https://www.eriwen.com/tools/awk-is-a-beautiful-tool/)
* [Awk tutorial](https://www.grymoire.com/Unix/Awk.html)
* [The awk programming language](https://www.pement.org/awk.htm)

## Links

<!-- markdownlint-disable MD034 -->
* https://example.com
<!-- markdownlint-enable MD034 -->
* [Example](https://example.com)
