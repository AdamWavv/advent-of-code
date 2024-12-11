package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
	"strings"
)

// Entry point for basic safety check
func BasicSafetyCheck() {
	processReports(evaluateReport)
}

// Entry point for safety check with adjustment logic
func AdjustedSafetyCheck() {
	processReports(evaluateWithAdjustment)
}

// Main logic to process reports and evaluate their safety
func processReports(safetyEvaluator func([]int) int) {
	reports := loadReports("input/task1.txt")
	totalSafeReports := 0

	for _, report := range reports {
		isSafe := safetyEvaluator(report)
		totalSafeReports += isSafe
	}

	fmt.Println("Total Safe Reports: ", totalSafeReports)
}

// Loads reports from a given file path
func loadReports(filePath string) [][]int {
	file, err := os.Open(filePath)
	if err != nil {
		log.Fatalf("Error opening file: %v", err)
	}
	defer file.Close()

	var reports [][]int
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		var reportValues []int
		values := strings.Fields(line)
		for _, value := range values {
			num, err := strconv.Atoi(value)
			if err != nil {
				log.Fatalf("Error converting string to integer: %v", err)
			}
			reportValues = append(reportValues, num)
		}
		reports = append(reports, reportValues)
	}

	if err := scanner.Err(); err != nil {
		log.Fatalf("Error reading file: %v", err)
	}

	return reports
}

// Checks if a report is safe based on strict increasing/decreasing logic
func evaluateReport(report []int) int {
	if len(report) < 2 {
		return 0 // A report with fewer than 2 levels cannot be validated
	}

	initialDifference := report[1] - report[0]
	isSafe := 1

	for i := 0; i < len(report)-1; i++ {
		currentDifference := report[i+1] - report[i]

		// Check for consistent direction and allowable difference range
		if currentDifference*initialDifference <= 0 || int(math.Abs(float64(currentDifference))) > 3 {
			isSafe = 0
			break
		}
	}

	return isSafe
}

// Attempts to adjust an unsafe report by removing one level
func evaluateWithAdjustment(report []int) int {
	isSafe := evaluateReport(report)
	if isSafe == 0 {
		for i := range report {
			modifiedReport := removeElementAt(report, i)
			if evaluateReport(modifiedReport) == 1 {
				return 1
			}
		}
	}
	return isSafe
}

// Removes an element at a specific index from an array
func removeElementAt(arr []int, index int) []int {
	newArr := make([]int, len(arr)-1)
	copy(newArr, arr[:index])
	copy(newArr[index:], arr[index+1:])
	return newArr
}

// Main function to execute the logic
func main() {
	// Choose the safety check method
	BasicSafetyCheck()
	AdjustedSafetyCheck() // Uncomment this to use the adjustment logic
}
