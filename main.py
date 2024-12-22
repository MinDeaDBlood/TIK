import os
import gettext
import locale

# Определяем язык
lang, _ = locale.getdefaultlocale()
language = lang if lang else "en"

# Установка путей к файлам переводов
locale_path = os.path.join(os.getcwd(), 'locales')

try:
    # Попытка загрузить перевод
    translation = gettext.translation('messages', localedir=locale_path, languages=[language])
    translation.install()
except FileNotFoundError:
    print(_("Translation file not found, falling back to English."))
    translation = gettext.NullTranslations()  # Установите пустой перевод, если нет перевода
