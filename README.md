feBuilder
=========

Набор скриптов для сборки html/css/js **в Linux** включает в себя:

* сборщик html файлов
* препроцессор SASS с фреймворком compass
* сборщик javascript файлов
* livereload

Установка
=========

Для работы скриптов необходимо установить Ruby, Python, Java (при использовании сжатия javascript)
Также нужны пакеты Ruby:

* [Guard](https://github.com/guard/guard)
* [Guard Compass Plug-in](https://github.com/guard/guard-compass)
* [Guard LiveReload](https://github.com/guard/guard-livereload)
* [Guard Shell](https://github.com/guard/guard-shell)

Настройка
=========

В файле htmlInclude.py находится скрипт сборки html. По умолчанию файлы .htm включаются в файлы .html

В файле config.rb настройки compass, для включения сжатия css раскомментировать строку output_style = :compressed

В файле Guardfile находятся настройки запуска скриптов, при изменении файлов. Для включения сжатия javascript файлов нужно скачать yuicompressor и раскомментировать строку `java -jar /путь/к/yuicompressor.jar ./prod/js/all.js -o ./prod/js/all.min.js && rm -rf ./prod/js/all.js`


Использование
=============

Для запуска нужно запустить guard в корне проекта

Для вставки html блоков используется конструкция @@include имя_файла.htm пример использования в файле src/index.html

Все .js файлы из директории src/js собираются в файл prod/js/all.js (или all.min.js при использовании сжатия)
