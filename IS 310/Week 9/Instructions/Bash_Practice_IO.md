\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*Practice Questions\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
  
0\. Write shell script to calculate sum with run time input  
  
#######################################################  
  
read -p "Enter first number: " num1  
read -p "Enter second number: " num2  
  
sum=$(( $num1 + $num2 ))  
  
echo "Sum is: $sum"  
  
#######################################################  
  
1\. How to write shell script that will add two nos, which are supplied as command line argument, and if this two nos are not given show error and its usage  
  
#######################################################  
  
if \[ $# -ne 2 \]  
then  
echo "Usage - $0 x y"  
echo " Where x and y are two nos for which I will print sum"  
exit 1  
fi  
echo "Sum of $1 and $2 is \`expr $1 + $2\`"  
  
#######################################################  
  
2\. Write Script to find out biggest number from given three nos. Nos are supplied as command line argument. Print error if sufficient arguments are not supplied.  
  
#######################################################  
  
if \[ $# -ne 3 \]  
then  
echo "$0: number1 number2 number3 are not given" >&2  
exit 1  
fi  
n1=$1  
n2=$2  
n3=$3  
if \[ $n1 -gt $n2 \] && \[ $n1 -gt $n3 \]  
then  
echo "$n1 is Biggest number"  
elif \[ $n2 -gt $n1 \] && \[ $n2 -gt $n3 \]  
then  
echo "$n2 is Biggest number"  
elif \[ $n3 -gt $n1 \] && \[ $n3 -gt $n2 \]  
then  
echo "$n3 is Biggest number"  
elif \[ $1 -eq $2 \] && \[ $1 -eq $3 \] && \[ $2 -eq $3 \]  
then  
echo "All the three numbers are equal"  
else  
echo "I can not figure out which number is biger"  
fi  
  
#######################################################  
  
3\. Write script to print nos as 5,4,3,2,1 using while loop.  
  
#######################################################  
  
i=5  
while test $i != 0  
do  
echo "$i  
"  
i=\`expr $i - 1\`  
done  
  
#######################################################  
  
4\. Write script to determine whether given file exist or not, file name is supplied as command line argument, also check for sufficient number of command line argument  
  
#######################################################  
  
if \[ $# -ne 1 \]  
then  
echo "Usage - $0 file-name"  
exit 1  
fi  
  
if \[ -f $1 \]  
then  
echo "$1 file exist"  
else  
echo "Sorry, $1 file does not exist"  
fi  
  
#######################################################  
  
5\. Write a Shell Bash Script for evaluate the status of a file/directory.  
  
#######################################################  
  
echo "Hello, what is the File/Directory name?"  
read FILE  
  
if \[ -e "$FILE" \]; then  
if \[ -f "$FILE" \]; then  
echo "$FILE is a regular file."  
fi  
if \[ -d "$FILE" \]; then  
echo "$FILE is a directory."  
fi  
if \[ -r "$FILE" \]; then  
echo "$FILE is readable."  
fi  
if \[ -w "$FILE" \]; then  
echo "$FILE is writable."  
fi  
if \[ -x "$FILE" \]; then  
echo "$FILE is executable/searchable."  
fi  
else  
echo "$FILE does not exist"  
exit 1  
fi  
exit  
  
#######################################################