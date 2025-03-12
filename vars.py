from diskcache import Cache

wiki_cache = Cache(size_limit=int(1.3e10), directory='/tmp/global-statistics')
def get_wiki_set():
    with open('wiki_list.txt', 'r') as f:
        wiki_set = f.read().splitlines()
    return wiki_set
