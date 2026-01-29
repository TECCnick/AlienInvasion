import csv

def load_dataset(file_path):
    dataset = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            dataset.append((row['prompt'], row['completion']))
    return dataset

def display_group_members():
    members = ["Member A"]
    print("Group Members:\n - Cada, Timothy Eli\n - Celibio Amory\n")

def display_description():
    description = """
    Welcome to EatGPT!
                                 ___
                          _/`.-'`.
                _      _/` .  _.'
       ..:::::.(_)   /` _.'_./
     .oooooooooo\ \o/.-'__.'o.
    .ooooooooo`._\_|_.'`oooooob.
  .ooooooooooooooooooooo&&oooooob.
 .oooooooooooooooooooo&@@@@@@oooob.
.ooooooooooooooooooooooo&&@@@@@ooob.
doooooooooooooooooooooooooo&@@@@ooob
doooooooooooooooooooooooooo&@@@oooob
dooooooooooooooEatGPToooooo&@@@ooooob
dooooooooooooooEatGPToooooo&@@oooooob
`doooooooooooooEatGPTooooooo&@ooooob'
 `doooooooooooooooooooooooooooooob'
  `doooooooooooooooooooooooooooob'
   `doooooooooooooooooooooooooob'
    `doooooooooooooooooooooooob'
     `doooooooooooooooooooooob'
      `dooooooooobodoooooooob'
       `doooooooob dooooooob'
         `"""""""' `""""""'

    This application provides information and advice on healthy eating, nutrition, and meal planning.
    You can ask questions related to diet, healthy recipes, and nutritional tips including how to lose weight!
    Type 'exit' to end the application.
    """
    print(description)

def get_response(prompt, dataset):
    for data_prompt, completion in dataset:
        if prompt.lower() in data_prompt.lower():
            return completion
    return "Sorry, I don't have an answer for that question."

def main():
    dataset = load_dataset('healthy_eating_dataset.csv')
    display_group_members()
    display_description()

    while True:
        user_input = input("\nWhat would you like to know about healthy eating?\n")
        if user_input.lower() == 'exit':
            print("Thank you for using the Healthy Eating Guide. Stay healthy!")
            break
        response = get_response(user_input, dataset)
        print(response)

if __name__ == "__main__":
    main()
