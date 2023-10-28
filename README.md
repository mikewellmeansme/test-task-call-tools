# Решение тестового задания call-tools

Описание задания приведено в task.md

Точка входа: `src/run.py`

Поддердживаемые команды:

* `change-speed path\to\file.wav -- speed` - изменяет скорость указанного аудиофайла в `speed` раз;

* `change-volume path\to\file.wav -- volume` - меняет громкость указанного аудиофайла на `volume` децибел;

* `recognize path\to\file.wav` - распознаёт речь в указанном файле и выводит на экран.

Вызовы и результаты основных функций логгируются в `logs\log.json` (путь к логам настраивается в `config.yaml`)

Для распознавания речи используется [Whisper](https://github.com/openai/whisper), модель `base`.

Известная проблема: change-volume при изменении скорости ещё и питчит звук. 