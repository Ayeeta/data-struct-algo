import json, itertools

class SearchByTag:
    
    def __init__(self, data_file, query_tag):
        with open(data_file) as data_file:
            self._data = json.load(data_file)
        self.query = query_tag      
    
    def data(self):
        return self._data['items']   
   
    def first(self):      
        movies = self.search()
        for movie in movies:
            return movie      

    def search(self):
        for item in self._data['items']:
            if self.query in item['tags']:
                yield item
                
        


searched = SearchByTag('data_json.json', '70s')

a = searched.data()
b = searched.search()
c = searched.first()
b
# for i in b:
#     print(i)