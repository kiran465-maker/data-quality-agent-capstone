import json, os
class MemoryAgent:
    def __init__(self,path='data/output/memory.json'):
        self.path = path
    def save(self, key, data):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path,'w') as f:
            json.dump({key:data}, f, indent=2)
