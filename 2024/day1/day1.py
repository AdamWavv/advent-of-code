# --- Day 1: Historian Hysteria ---
# Link: https://adventofcode.com/2024/day/1
# The task is to calculate the sum of distances  of sorted list.

from enum import unique
from utils.logger import get_logger
import itertools
from collections import Counter


logger = get_logger(__name__)

class HistorianHysteria:
    
    @staticmethod
    def get_input(file_path):
        logger.info(f"Attempting to read data from file: {file_path}")
            
        data1 = []
        data2 = []
        try:
            with open(file_path, 'r') as file:
                # Read each line and convert to an integer after stripping whitespace
                input_file = file.readlines()
                for line in input_file:
                    numbers = [int(x) for x in line.split() if x.strip()]
                    data1.append(numbers[0])
                    data2.append(numbers[1])
                logger.info(f"Successfully read data from {file_path}")
                return data1, data2
        except FileNotFoundError:
            logger.error(f"File not found: {file_path}")
        except Exception as e:
            logger.error(f"Error reading file {file_path}: {e}")
        
        return data1, data2
    @staticmethod
    def task1(list1, list2):
        logger.info(f"HistorianHysteria.task1: start")
        if list1 != sorted(list1):
            list1.sort()
        if list2 != sorted(list2):
            list2.sort()
        # Using a generator expression to sum the absolute differences directly
        return sum(abs(x1 - x2) for (x1, x2) in itertools.zip_longest(list1, list2, fillvalue=0))
    
    @staticmethod
    def task2(list1, list2):
        logger.info(f"HistorianHysteria.task2: start")
        output = []

        # Initialize an empty set to track seen elements
        seen = set()
        # Create a Counter for list2 to count occurrences of each element
        count_dict = Counter(list2)
        # Generator expression to yield unique values from list1
        # It checks if the element has already been seen by looking it up in the 'seen' set
        # If not seen, it adds the element to the 'seen' set and yields the value
        unique = (val for val in list1 if val not in seen and not seen.add(val))
        for i in unique:
            output.extend([i] * count_dict[i])
        return sum(output)





def main():
    # Initialize HistorianHysteria instance
    solver = HistorianHysteria()

    # Get directory path from environment variable
    directory_task1 = 'input/task1.txt'
    directory_task1 = 'input/task2.txt'
    list1, list2 = solver.get_input(directory_task1)
    task1 = solver.task1(list1, list2)
    task2 = solver.task2(list1, list2)
    logger.info(f"Answer for task1 is: {task1} and for task2 is: {task2}")



if __name__ == "__main__":
    main()
