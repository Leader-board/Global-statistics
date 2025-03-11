from diskcache import Cache

wiki_cache = Cache(size_limit=2**33, directory='/mnt/nfs/secondary-scratch/global-statistics')
def get_wiki_set():
    with open('wiki_list.txt', 'r') as f:
        wiki_set = f.read().splitlines()
    return wiki_set
