import openai
from datetime import datetime

# Set your OpenAI API key
api_key = "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"
openai.api_key = api_key

# Input and output files
input_file = "combined_text.txt"
summary_output_file = f"data/summary_{datetime.now().strftime('%d-%m-%Y')}.txt"
minutes_output_file = f"data/minutes_{datetime.now().strftime('%d-%m-%Y')}.txt"
title_output_file = f"data/title_{datetime.now().strftime('%d-%m-%Y')}.txt"

# Read the content of the input file
with open(input_file, "r") as file:
    content = file.read()

# Generate a summary using OpenAI's API
summary_prompt = "Summarize the following text:\n" + content
summary_result = openai.Completion.create(
    engine="text-davinci-003",
    prompt=summary_prompt,
    max_tokens=150  # Adjust the number of tokens for the summary length
)

# Save the summary to the output file
summary = summary_result.choices[0].text.strip()
with open(summary_output_file, "w") as file:
    file.write(summary)

# Generate meeting minutes using OpenAI's API
minutes_prompt = "Generate meeting minutes from the following text with bullet:\n" + content
minutes_result = openai.Completion.create(
    engine="text-davinci-003",
    prompt=minutes_prompt,
    max_tokens=400  # Adjust the number of tokens for the minutes length
)

# Format meeting minutes with bullet points
minutes_text = minutes_result.choices[0].text.strip()
# Splitting the text into bullet points
minutes_list = minutes_text.split("\n")
formatted_minutes = "\n".join(f"{point}" for point in minutes_list)

# Save the formatted meeting minutes to the output file
with open(minutes_output_file, "w") as file:
    file.write(formatted_minutes)

# Generate a title using OpenAI's API
title_prompt = "Generate an appropriate title for the following text:\n" + content
title_result = openai.Completion.create(
    engine="text-davinci-003",
    prompt=title_prompt,
    max_tokens=30  # Adjust the number of tokens for the title length
)

# Save the generated title to the output file
title = title_result.choices[0].text.strip()
with open(title_output_file, "w") as file:
    file.write(title)