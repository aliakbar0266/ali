#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Import gtts library for converting txt to audio 
# from gtts we need gTTS
# to import that we need to install gtts , pip install gtts


from gtts import gTTS 
  

  
# The text that you want to convert to audio 
#Input I if you wish to type a text to be converted to a audio file,
#and input T if you wish to read a text file from yoour computer ands convert it
# to an audio file")


request=input(" input I or T:   ") 
if request=="I":
    your_text = input("Import a text you want to convert to audio file    ")
elif request=="T":
    text= open("C://Users//ALI Project//My_Text.txt", "r")
    your_text=text.read().replace("\n", " ")


# Choose the language you wish to convert your text to 
language = 'en'
  
# now pass the text file, your language and your preference for speed of the audio
# file to the gTTS function
Converted_file= gTTS(text=your_text , lang=language, slow=False) 
  
# Save the converted file in a mp3 format

Converted_file.save("My_File.mp3") 






