class Source:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,name,description,url,category,language,country):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country



class Articles:
    
    def __init__(self,author,title,description,url,urlToImage,publishedAt):
        self.author = author
        self.title =title
        self.description = description
        self.url = url
        self.urlToImage =urlToImage
        self.publishedAt = publishedAt