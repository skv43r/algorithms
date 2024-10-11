from collections import deque

graph = {}
graph['Me'] = ['Alice', 'Bob', 'Kler']
graph['Bob'] = ['Anudge', 'Peggie']
graph['Alice'] = ['Peggie']
graph['Kler'] = ['Tom', 'Jonny']
graph['Anudge'] = []
graph['Peggie'] = []
graph['Tom'] = []
graph['Jonny'] = []

def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(f"{person} is mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    return False

search('Me')

