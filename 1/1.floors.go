package main 
import (
	"fmt"
	"strings"
	"io/ioutil"
)

func get_floor() int {
	filename := "input.txt"
	contents, _ := ioutil.ReadFile(filename)

	upstairs := strings.Count(string(contents), "(") // before & after each rune
	downstairs := strings.Count(string(contents), ")") // before & after each rune
	floor := upstairs - downstairs
	return floor
}

func main() {

	fmt.Println(fmt.Sprintf("Floor: %d", get_floor()))
}