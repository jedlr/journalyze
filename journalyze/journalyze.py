import csv
import random


class DailyPrompt:
    # initialize the object and load the prompts from a CSV file.
    def __init__(self, prompts_file):
        self.prompts_file = prompts_file
        self.prompts = []
        with open(prompts_file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                self.prompts.append(row[0])

    def get_prompt(self):
        """
        This function randomly selects a prompt
        from the list of prompts and return it to the user.
        Args:
            self
        Returns:
            prompt (data)
        """
        return random.choice(self.prompts)

    def add_prompt(self, prompt):
        """
        This function adds a new prompt to the list of prompts.
        Args:
            Prompt to be appended
        Returns:
            None: see note
        Note: appends the given prompt to the csv file of prompts
        """
        self.prompts.append(prompt)

    def remove_prompt(self, prompt):
        """
        This function removes a prompt from the list of prompts.
        Args:
            Prompt to be removed
        Returns:
            None: see note
        Note: removes the given prompt from the list of prompts
        """
        self.prompts.remove(prompt)
