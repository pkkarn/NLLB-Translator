from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import sys

model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")
tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M")
#src_lang="eng_Latn", tgt_lang='hin_Deva'
def translateMyWord(input, src_lang, tgt_lang):
    translator = pipeline('translation', model=model, tokenizer=tokenizer, src_lang=src_lang, tgt_lang=tgt_lang, max_length = 500)
        #f=open("guru99.txt","a+")

    output = translator(input)

    return output[0]['translation_text']

def textCount(input):
    return len(input)
