# README file for Lesson Plan Generators

We used Python to create a set of prompts and we created a function
that iterates through the grade levels.

## Seed Prompt

Our "Seed Prompt" is a prompt that generates Python code that iterates through the prompts for each activity.

```linenums="0"

Create a Python function called generate_discussion that will call the OpenAI API using the GPT-4 model.
Iterate through three grade levels (5th, 9th and 11th grades) for two topic prompts
("Batteries" and "Motors").

topics = ["Batteries", "Motors", "Sensors"]
grade_levels = [5, 7, 9]

for topic in topics:
    for grade_level in grade_levels:
       generate_discussion(topic, grade_level)

The entire prompt should look like this:

"Generate a single paragraph description of a discussion between a teacher and a students about robotics.  The topic is {$topic} and the grade level is {$grade_level}.  

The generate_discussion function can assume that the OPENAI_API_KEY
is in an global variable called OPENAI_API_KEY.
```

[ChatGPT Seed Generator](https://chat.openai.com/share/b9c90cce-8a3e-4568-9ffd-662be2420499)