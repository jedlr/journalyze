from unittest.mock import patch
import unittest
import csv
from io import StringIO
from unittest.mock import patch
from journalyze import *

#def test_hello():
    #assert hello() == "Hello, world!"


#@patch('builtins.print')
#def test_print_hello(mock_print):
    #print_hello()
    #assert mock_print.call_args.args == ("Hello, world!",)


class TestDailyPrompt(unittest.TestCase):
    def setUp(self):
        self.prompts_file = 'test_prompts.csv'
        self.prompts = ['What was your favorite part of today?', 'What are you grateful for today?']
        with open(self.prompts_file, 'w', newline='') as f:
            writer = csv.writer(f)
            for prompt in self.prompts:
                writer.writerow([prompt])
        self.dp = DailyPrompt(self.prompts_file)

    def tearDown(self):
        self.dp.save_prompts()
        self.dp = None

    def test_init(self):
        self.assertEqual(self.dp.prompts, self.prompts)

    def test_get_prompt(self):
        prompt = self.dp.get_prompt()
        self.assertIn(prompt, self.prompts)

    def test_add_prompt(self):
        new_prompt = 'What is something you learned today?'
        self.dp.add_prompt(new_prompt)
        self.assertIn(new_prompt, self.dp.prompts)

    def test_remove_prompt(self):
        prompt_to_remove = 'What was your favorite part of today?'
        self.dp.remove_prompt(prompt_to_remove)
        self.assertNotIn(prompt_to_remove, self.dp.prompts)

    @patch('sys.stdout', new_callable=StringIO)
    def test_save_prompts(self, mock_stdout):
        self.dp.add_prompt('What was the highlight of your week?')
        self.dp.save_prompts()
        with open(self.prompts_file, 'r') as f:
            reader = csv.reader(f)
            new_prompts = [row[0] for row in reader]
        self.assertEqual(new_prompts, self.dp.prompts)
        expected_output = 'Prompts saved to test_prompts.csv\n'
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()