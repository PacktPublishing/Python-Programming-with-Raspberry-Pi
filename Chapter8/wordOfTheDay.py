#!/usr/bin/python3

from wordnik import *

# sign up for an API key
API_KEY = 'API_KEY'
apiUrl = 'http://api.wordnik.com/v4'

if __name__ == "__main__":
  client = swagger.ApiClient(API_KEY, apiUrl)
  wordsApi = WordsApi.WordsApi(client)
  example = wordsApi.getWordOfTheDay()
  print("The word of the day is %s" % example.word)
  print("The definition is %s" %example.definitions[0].text)