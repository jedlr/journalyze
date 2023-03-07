import unittest
import csv
from journalyze import DailyPrompt

class TestDailyPromptIntegration(unittest.TestCase):
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

    def test_integration(self):
        # Check that the initial prompts are in the list
        self.assertEqual(self.dp.prompts, self.prompts)

        # Check that a prompt can be retrieved
        prompt = self.dp.get_prompt()
        self.assertIn(prompt, self.prompts)

        # Check that a new prompt can be added
        new_prompt = 'What is something you learned today?'
        self.dp.add_prompt(new_prompt)
        self.assertIn(new_prompt, self.dp.prompts)

        # Check that a prompt can be removed
        prompt_to_remove = 'What was your favorite part of today?'
        self.dp.remove_prompt(prompt_to_remove)
        self.assertNotIn(prompt_to_remove, self.dp.prompts)

        # Check that the prompts can be saved to a file and loaded again
        self.dp.add_prompt('What was the highlight of your week?')
        self.dp.save_prompts()
        new_dp = DailyPrompt(self.prompts_file)
        self.assertEqual(new_dp.prompts, self.dp.prompts)

if __name__ == '__main__':
    unittest.main()
