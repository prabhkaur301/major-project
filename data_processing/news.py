import string
import spacy

nlp = spacy.load("en_core_web_lg")

######################## ~news input processing ############################################
def punctuation_removal(text):
    all_list = [char for char in text if char not in string.punctuation]
    clean_str = ''.join(all_list)
    return clean_str

def news_detect(news):
  input_data=punctuation_removal(news)
  vectorised_input_data=nlp(input_data).vector
  data_2D= vectorised_input_data.reshape(1, -1)
  return data_2D
####################### ~news data processing end ###########################################