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

    def get_prompt_easy(self):
        """
        This function randomly selects an EASY/SHORT prompt
        from the list of prompts and return it to the user.
        Args:
            self
        Returns:
            prompt (data)
        Note: an easy prompt is defined here as
        a prompt with less than 11 words
        """
        prompt = random.choice(self.prompts)
        if len(prompt.split()) < 11:
            return prompt

    def get_prompt_hard(self):
        """
        This function randomly select a HARD/LONG prompt
        from the list of prompts and return it to the user.
        Args:
            self
        Returns:
            prompt (data)
        Note: a hard prompt is defined here as a prompt with more than 11 words
        """
        prompt = random.choice(self.prompts)
        if len(prompt.split()) > 11:
            return prompt

    def get_prompt_num(self, num_prompts):
        """
        This function returns a number of prompts
        Args:
            self, num_prompts (int) (number of prompts user wants)
        Returns:
            list of prompts (data)
        """
        num_prompts = int(input("How many prompts would you like? "))
        return random.choices(self.prompts, k=num_prompts)

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
