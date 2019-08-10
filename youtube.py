#!/usr/bin/env python3
import requests
import os
from sys import argv,exit
from bs4 import BeautifulSoup


def play(query):
    query=query.replace(' ','+')

    # Search for the song youtube
    url='https://www.youtube.com/results?search_query='+query
    source_code = requests.get(url, timeout=15)
    plain_text=source_code.text
    soup=BeautifulSoup(plain_text,"html.parser")

    # scrape the link of first video with that song name
    songs=soup.findAll('div',{'class':'yt-lockup-video'})
    
    # print(songs[0])

    song=songs[0].contents[0].contents[0].contents[0]
    
    # print(song)

    link=song['href']

    # play it by visiting the link
    firefox_start = "firefox http://www.youtube.com"+link
    
    os.system(firefox_start)


play('kgf songs')