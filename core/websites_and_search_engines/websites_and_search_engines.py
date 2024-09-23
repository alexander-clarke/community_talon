import webbrowser
from urllib.parse import quote_plus

from talon import Module

from ..user_settings import get_list_from_csv

mod = Module()
mod.list("website", desc="A website.")
mod.list(
    "search_engine",
    desc="A search engine.  Any instance of %s will be replaced by query text",
)

# mod.list("subreddit", desc="A subreddit")

# subreddit_defaults = {
#   "Dota": "Dota2",
#   "hardware": "hardware",
#   "gamedev": "gamedev",
#   "no context pics": "nocontextpics",
# }

# subreddit_list = get_list_from_csv(
#   "subreddits.csv",
#   headers = ("subreddit", "spoken name"),
#   default = subreddit_defaults,
# )

# subreddit_websites = {"sub " + k: "https://old.reddit.com/r/" + v for (k, v) in subreddit_list.items()}

# websites.update(subreddit_websites)


@mod.action_class
class Actions:
    def open_url(url: str):
        """Visit the given URL."""
        webbrowser.open(url)

    def search_with_search_engine(search_template: str, search_text: str):
        """Search a search engine for given text"""
        url = search_template.replace("%s", quote_plus(search_text))
        webbrowser.open(url)
