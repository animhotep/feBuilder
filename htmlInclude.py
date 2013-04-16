# -*- coding: utf-8 -*-
import os
#заносим блоки для включения в словарь
d = {}
for files in os.listdir("src/."):
	if files.endswith(".htm"):
		r = open("src/"+files,'r')
		block = r.read()
		d[files] = block
#находим файлы вставки блоков
for files in os.listdir("src/."):
	if files.endswith(".html"):
		w = open("prod/"+files,'w')
		for s in open("src/"+files):
			#находим строки, начинающиеся с @@include
			if s.startswith('@@include'):
				#находим имя блока для замены
				blockName = s.replace('@@include ', '')
				blockName = blockName.rstrip('\n')
				#делаем замену, если в словаре есть нужный блок
				if blockName in d:
					s = d[blockName]+'\n'
			#записываем новый файл
			w.write(s)
		w.close()