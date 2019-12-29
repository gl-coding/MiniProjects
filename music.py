import time
import pygame
import os 
import random

def readList():
	music_list = []
	with open("music.list", "r") as r:
		for line in r:
			if os.path.exists(line):
				os.remove(line)

def writeList(line):
	with open("music.list", "a") as w:
		w.write(line+"\n")

def playSong(filename):
	file = filename
	pygame.mixer.init()

	track = pygame.mixer.music.load(file)

	pygame.mixer.music.play(loops=0, start=0.0)
	#time.sleep(40)
	# pygame.mixer.music.stop()
	# counter = 0
	while 1 == pygame.mixer.music.get_busy():
		time.sleep(1)
		# counter += 1
		# if counter > 10:
		# 	pygame.mixer.music.stop()
	# return counter

def playRandomMusic():
	dir = "d:\music"
	music_list = []
	file_list = os.listdir(dir)
	for f in file_list:
		path = os.path.join(dir, f)
		#print path
		music_list.append(path)
	music = random.choice(music_list)
	print music
	try:
		playSong(music)
	except Exception as e:
		print e

def listFiles(dir):
	music_list = []
	file_list = os.listdir(dir)
	for f in file_list:
		path = os.path.join(dir, f)
		print path
		music_list.append(path)
	while True:
		ran
		timelong = playSong(path)
		print timelong
		if timelong < 10:
			writeList(path)

if __name__ == "__main__":
	file=r'd:\music\15.mp3'
	dir = "d:\music"
	#playSong(file)
	#listFiles(dir)
	#os.remove("d:\\music\\00000008.mp3")
	#readList()
	playRandomMusic()