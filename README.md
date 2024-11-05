[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=16963180)
# Markov Chains

Markov Chains are a simple way to model the probability of a sequence of events. In the context of text generation, a Markov Chain can be used to generate text that is similar to a given corpus. The basic idea is to build a dictionary of transitions between words in the corpus, and then use this dictionary to generate new text.

## Requirements

Given the basic Markov Chain code in [markov.py](markov.py), your task is to enhance the code to allow for more complex Markov Chains. Specifically, you will implement the following:

### Expand the Corpus

Update the `text` variable to use a larger corpus (i.e. a full chapter from a book, a long article, or the entire text of a given book from [Project Gutenberg](https://www.gutenberg.org/)). You may pull this data directly from a file, a URL, or embed it directly in your code (the latter is not recommended for large texts, however the choice is yours).

### Enhance the Tokenizer

Update the Tokenizer (the Markov Chain builder) to take punctuation into account. For example, after splitting on the spaces (this code):

```python
words = text.split()
for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    if current_word not in transitions:
        transitions[current_word] = []
    transitions[current_word].append(next_word)
```
… split out the punctuation and add them as separate tokens to the `transitions` dictionary. This should theoretically create more predictable sentence structure with more proper punctuation.

### Implement User Input

Accept user input, allowing the user to specify the first word to start when executing the script from the command line, followed by the number of words to generate. For example:

```bash
python3 markov.py "The" 100
```

### Text Cleanup

Implement basic text cleanup (i.e. capitalizing the first word of each sentence, ensuring proper spacing around punctuation, etc.), by enhancing the `generate_text()` function:

```python
def generate_text(start_word, num_words):
    current_word = start_word
    result = [current_word]
    for _ in range(num_words - 1):
        if current_word in transitions:
            next_word = random.choice(transitions[current_word])
            result.append(next_word)
            current_word = next_word
        else:
            break
    return " ".join(result)
```

## Testing

To test your implementation, you should be able to run the script from the command line and generate text based on a given starting word and number of tokens to generate. For example:

```bash
python3 markov.py "The" 100
```

Given the freedom to choose your own corpus, there are no automated tests for this assignment. That said, the above command will be used to evaluate your implementation.