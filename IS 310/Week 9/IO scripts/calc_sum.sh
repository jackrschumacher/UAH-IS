# Calculate the sum of 2 numbers 

echo "Sum Number program"
read -p "Please enter the first number that you would like to sum: " number1
read -p "Please enter the second number that you would like to sum: " number2

sum=$(($number1+$number2))

echo "The sum of $number1 and $number2 is $sum"