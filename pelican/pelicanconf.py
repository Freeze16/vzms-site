# coding: utf-8

SITENAME = {
    "full": "Воронежская зимняя математическая школа",
    "short": "ВЗМШ",
}
SITEURL = "vzms.kmm-vsu.ru"

AUTHOR = "vzms@mail.ru"
DESCRIPTION = "Воронежская зимняя математическая школа C.Г. Крейна"
KEYWORDS = "Воронежская зимняя математическая школа, ВЗМШ"
YEAR = "2026"

THEME = "theme"

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["participants_list"]

SLUGIFY_SOURCE = "basename"
PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"

PAGE_ORDER_BY = "order"
STATIC_PATHS = ["files"]

# Disable generations some files
ARCHIVES_SAVE_AS = None
AUTHORS_SAVE_AS = None
CATEGORIES_SAVE_AS = None
FEED_ALL_ATOM = None
TAGS_SAVE_AS = None
