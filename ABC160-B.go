package main

import "fmt"

func main(){
	var x, xRemain, delightVal int

	fmt.Scan(&x)

	xRemain = x % 500
	delightVal = (x - xRemain)*2
	delightVal += (xRemain - xRemain % 5)

	fmt.Println(delightVal)
}