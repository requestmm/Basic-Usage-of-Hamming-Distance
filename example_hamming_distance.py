# Basic usage of Hamming Distance to analyze cities wrote on XLSX file.


import pandas as pd
from scipy.spatial.distance import hamming

df = pd.read_excel(R"cities_MG_Brazil.xlsx")

target_word = "Água Boa"
target_word_length = len(target_word)

for reference_word in df["CITY_NAME"]:
    reference_word_length = len(reference_word)
    diff = target_word_length - reference_word_length
    if diff > 0:
        reference_word = reference_word = reference_word + "_" * diff
    elif diff < 0:
        reference_word = reference_word[:diff]

    target_word = list(target_word)
    reference_word = list(reference_word)
    

    hamming_distance = hamming(target_word, reference_word)

    print(target_word, reference_word, hamming_distance)
