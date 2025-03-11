from diskcache import Cache

wiki_cache = Cache(size_limit=int(4e9))
def get_wiki_set():
    with open('wiki_list.txt', 'r') as f:
        wiki_set = f.read().splitlines()
    return wiki_set
