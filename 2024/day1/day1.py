# --- Day 1: Historian Hysteria ---
# Link: https://adventofcode.com/2024/day/1
# The task is to calculate the sum of distances  of sorted list.

import os
from dotenv import load_dotenv
from utils.logger import get_logger
import requests
import itertools

import numpy as np

logger = get_logger(__name__)

class HistorianHysteria:

    @staticmethod
    def get_problem_description(url, session_cookie):
        headers = {"Cookie": f"session={session_cookie}"}
        logger.info("HistorianHysteria.get_problem_description: Getting url request.")
        response = requests.get(url=url, headers=headers)
        
        if response.status_code == 200:
            logger.info("Access succesful")
        else:
            logger.warning(f"Access denied, status code {response.status_code}")
    
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
    def total_distance(list1, list2):
        list1.sort()
        list2.sort()

        output = [abs(x1 - x2) for (x1, x2) in itertools.zip_longest(list1, list2)]
        return(sum(output))

def main():
    # Initialize HistorianHysteria instance
    solver = HistorianHysteria()

    # Get directory path from environment variable
    directory = 'input/data.txt'
    list1, list2 = solver.get_input(directory)
    print(solver.total_distance(list1, list2))






if __name__ == "__main__":
    main()
