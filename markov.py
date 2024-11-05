import random
import argparse
import os


def parse_file(path): # Turns a file into a single string
    file = open(path, "r")
    parsed = " ".join([i for i in file.readlines()])
    file.close()
    return parsed

def generate_text(start_word, num_words): # Generate the text based on the Markov chain
    current_word = start_word
    result = [current_word]
    for _ in range(num_words - 1):
        if current_word in transitions:
            next_word = random.choice(transitions[current_word])
            result.append(next_word)
            current_word = next_word
        else:
            break
    return clean(" ".join(result))

def clean(text): # Formats the text, capitalizing sentences and dealing with punctuation
    result = ""
    text = text.split()
    for pos, word in enumerate(text):
        if text[pos - 1] in sentence_end or pos == 0 or word == "i": # If the previous word was the end of a sentence, this is the first word, or it is "I",
            word = word.capitalize() # Then capitalize the word
        if word not in punctuation and not pos == 0: # Add a space before the word if it's not punctuation or the first word
            word = " " + word
        result += word
    return result
        


parser = argparse.ArgumentParser() # Gets the text, first word, and length of the response from the user
parser.add_argument("text")
parser.add_argument("start")
parser.add_argument("length", type=int)
args = parser.parse_args()

if os.path.isfile(args.text): # If the text is a file, parse it
    text = parse_file(args.text)
else: # Otherwise, it's just a string
    text = args.text

transitions = {}

words = text.lower().split() # Make the text lowercase and split it into individual words

i = 0
punctuation = [".", ",", "!", ";", '"', "'", "?", ":", "-"]
sentence_end = ".!?"

while i < len(words): # Split the punctuation into individual words
    word = words[i]
    for punct in punctuation:
        if word.startswith(punct) or word.endswith(punct): # If the word has punctuation attatched to it (done to not split up words like "don't")
            words.pop(i) # Remove the word
            words.insert(i, punct) # and replace it with the word and punctuation seprately
            words.insert(i, word.replace(punct, ""))
            i += 1
    i += 1


for i in range(len(words) - 1): # Build the Markov chain
    current_word = words[i]
    next_word = words[i + 1]
    if current_word not in transitions:
        transitions[current_word] = []
    transitions[current_word].append(next_word)

print(generate_text(args.start, args.length))