# import random
# from nltk.translate.bleu_score import sentence_bleu

# # Function to generate suggestions
# def generate_suggestions(sentence):
#     # Split sentence into words
#     words = sentence.split()
#     suggestions = []
#     max_confidence = 0
#     # Generate 5 shuffled sentences
#     for i in range(5):
#         random.shuffle(words)
#         shuffled_sentence = ' '.join(words)
#         suggestions.append(shuffled_sentence)
#         # Calculate confidence score using sentence_bleu
#         confidence = sentence_bleu([sentence], shuffled_sentence)
#         # Update max_confidence and correct sentence
#         if confidence > max_confidence:
#             max_confidence = confidence
#             correct_sentence = shuffled_sentence
#     # Print suggestions
#     print("Original sentence: ", sentence)
#     print("Suggestions: ")
#     for suggestion in suggestions:
#         print(suggestion)
#     print("Correct Sentence: ", correct_sentence)

# # Test the function
# generate_suggestions("This is a test sentence.")
