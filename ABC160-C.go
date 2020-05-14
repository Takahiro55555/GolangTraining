/*
* Golangの練習
*
*/

package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
)

func main(){
	sc := bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)

	// 1行目
	k := nextInt(sc)
	n := nextInt(sc)

	// 2行目
	var a = make([]int, n+1)
	for i := 0; i < n; i++ {
		a[i] = nextInt(sc)
	}
	a[n] = k+a[0]

	// NOTE: REの原因個所の特定
	maxCost := 0
	for i := 0; i < n; i++ {
		tmp := a[i+1] - a[i]
		if tmp > maxCost {
			maxCost = tmp
		}
	}
	fmt.Println(k - maxCost)
}

func nextInt(sc *bufio.Scanner) int {
	sc.Scan()
	t, _ := strconv.Atoi(sc.Text())
	return t
}