wiki_cache = {}
def get_wiki_set():
    with open('wiki_list.txt', 'r') as f:
        wiki_set = f.read().splitlines()