#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
+++++++++++++++++++++++++++++++++++++
བསེ་ཁྲབ་སྐྱབས་ཀྱིས་སྤྱི་ལོ་༢༠༡༧་ལོའི་ཟླ་བ་༦་པའི་ཚེས་༡༣་ལ་ཤར་མར་བྲིས།
དཔྱད་གཞིའི་ཡིག་ཆ༼TSRM藏文拼写检查算法༽གཙོ་བོར་བཟུང་།

+++++++++++++++++++++++++++++++++++++
"""

import re


con = r"^(རྐ|རྒ|རྔ|རྗ|རྙ|རྟ|རྡ|རྣ|རྦ|རྨ|རྩ|རྫ|ལྐ|ལྒ|ལྔ|ལྕ|ལྗ|ལྟ|ལྡ|ལྤ|ལྦ|ལྷ|སྐ|སྒ|སྔ|སྙ|སྟ|སྡ|སྣ|སྤ|སྦ|སྨ|སྩ|\
        ཀྱ|ཁྱ|གྱ|པྱ|ཕྱ|བྱ|མྱ|ཀྲ|ཁྲ|གྲ|ཏྲ|ཐྲ|དྲ|ནྲ|པྲ|ཕྲ|བྲ|མྲ|ཤྲ|སྲ|ཧྲ|ཀླ|གླ|བླ|ཟླ|རླ|སླ|ཀྭ|ཁྭ|གྭ|ཉྭ|དྭ|ཚྭ|ཞྭ|\
        ཟྭ|རྭ|ལྭ|ཤྭ|ཧྭ|གྲྭ|ཕྱྭ|རྩྭ|རྐྱ|སྐྱ|སྐྲ|རྒྱ|སྒྱ|སྒྲ|སྣྲ|སྤྱ|སྤྲ|སྦྱ|སྦྲ|རྨྱ|སྨྱ|སྨྲ|གཅ|གཉ|གཏ|གད|གན|གཙ|གཞ|གཟ|\
        གཡ|གཤ|གས|དཀ|དཀྱ|དཀྲ|དག|དགྲ|དགྱ|དང|དཔ|དཔྱ|དཔྲ|དབ|དབྱ|དབྲ|དམ|དམྱ|བཀ|བཀྱ|བཀྲ|བཀླ|བརྐ|\
        བསྐ|བརྐྱ|བསྐྱ|བསྐྲ|བག|བགྱ|བགྲ|བརྒ|བསྒ|བརྒྱ|བསྒྱ|བསྒྲ|བསྔ|བརྔ|བཅ|བརྗ|བརྙ|བསྙ|བཏ|བརྟ|བསྟ|བལྟ|བད|\
        བརྡ|བསྡ|བལྡ|བརྣ|བསྣ|བཙ|བརྩ|བརྫ|བཞ|བཟ|བཟླ|བརླ|བཤ|བས|བསྲ|བསླ|འག|འགྱ|འགྲ|འཁ|འཁྱ|འཁྲ|འཆ|\
        འཇ|འཐ|འད|འདྲ|འཕ|འཕྱ|འཕྲ|འབ|འབྱ|འབྲ|འཚ|འཛ|མཁ|མཁྱ|མཁྲ|མག|མགྲ|མང|མཆ|མཇ|མཉ|མད|མན|\
        མཚ|མཛ|ཊ|ཎ|བྷ|ཧྥ|པདྨ|ཀརྨ|ཀ|ཁ|ག|ང|ཅ|ཆ|ཇ|ཉ|ཏ|ཐ|ད|ན|པ|ཕ|བ|མ|ཙ|ཚ|ཛ|ཝ|ཞ|ཟ|འ|ཡ|ར|\
        ལ|ཤ|ས|ཧ|ཨ|ཊ|ཎ|བྷ|ཧྥ|པདྨ|ཀརྨ)"
vowel = r"([\u0F71])?[\u0F71-\u0F8F]"
postfix = r"(གས|ངས|བས|མས|ནད|རད|ལད|འུའི|འི|འུ|འོ|འང|འམ|འེ|ག|ང|ད|ན|བ|མ|འ|ར|ལ|ས|ཊ|ཎ)$"

SUB      = re.compile(r"([^\u0F0B\u0F40-\u0FBC]+)")
SUB_     = re.compile(r"^([^\u0F0B\u0F40-\u0FBC]+)$")
CON      = re.compile(con)
CON_     = re.compile(con+"$")
VOWEL    = re.compile(vowel)
VOWEL_   = re.compile(con+vowel+"$")
POSTFIX  = re.compile(con+postfix)
POSTFIX_ = re.compile(con+vowel+postfix)

SPECIAL = re.compile(r"^(གཅ|གཉ|གཏ|གཙ|གཞ|གཟ|གཡ|གཤ|དཀ|དཔ|བཀ|བཅ|བཏ|བཙ|བཞ|བཟ|\
                     བཤ|འཁ|འཆ|འཇ|འཐ|འཕ|འཚ|འཛ|མཁ|མཆ|མཇ|མཉ|མཐ|མཚ|མཛ)$")


class TSRM(object):
    def __init__(self):
        a = 1

    def is_word(self,word):
        self.word = re.sub("་","",word)
        if CON.search(self.word):
            if not CON_.search(self.word):
                if VOWEL.search(self.word):
                    if POSTFIX_.search(self.word):
                        return True
                    elif VOWEL_.search(self.word):
                        return True
                    else:
                        return False
                else:
                    if POSTFIX.search(self.word):
                        return True
                    else:
                        return False
            else:
                if SPECIAL.search(self.word):
                    return False
                else:
                    return True
        else:
            return True

    def is_sent(self,text):
        self.text = self.sub(text)
        l1 = self.split(self.text)
        l2 = map(self.is_word,l1)
        self.words = list(zip(l1,l2))
        words = []
        for w,f in self.words:
            if f:
                words.append(w)
            else:
                words.append(w+"XX")
        return "་".join(words)

    def sub(self,sent):
        sent = SUB.sub(r"་\1་",sent)
        sent = sent.strip("་")
        return sent

    def split(self,sent):
        ll = sent.split("་")
        ll = [l.strip() for l in ll if l]
        return ll



if __name__ == "__main__":

    TT = TSRM()
    
    se = "༄༅།།ཀརྨ་པ་སྐུ་ཕྲེང་བཅུ་བདུན(1955)པསི་ཞལ་གདམས་གནངས།"
    print(TT.is_sent(se))
    words = ["སྐྱིད","གཏཀ","གཅ","འདུག","འད","གོ","འདག","སྤྲའུ","གཏོཊ","བྷོད","ཧྥུ","མའེ",\
            "ཊཱ","ཎི","དཱི","མེེ","གཅངས","ཐྲེད","ཀརྨ",'བསྟུ','ཀརྨབས',"ཏོོ","མངོན","ལགགཞན","མཐུའུ","དཔིའ","མཁག","ཁྱེའུས"]
    for w in words:
        print(w,TT.is_word(w))


   





