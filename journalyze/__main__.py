from .journalyze import DailyPrompt

if __name__ == "__main__":
    dp = DailyPrompt('journalyze/prompts.csv')
   
    prompt = dp.get_prompt()
    print(prompt)
   
    easy_prompt = dp.get_prompt_easy()
    print(easy_prompt)

    hard_prompt = dp.get_prompt_hard()
    print(hard_prompt)

    num_prompts = int(input("How many prompts would you like? "))
    multiple = dp.get_prompts_num(num_prompts)
    for multiple in dp:
        print(multiple)

    dp.add_prompt('What was something you learned today?')

    dp.remove_prompt('What was your favorite memory from last year?')
