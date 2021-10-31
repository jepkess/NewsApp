class Article:
    '''
    Articles class to define Articles Objects
    '''

    def __init__(self,author,title,description,url,image,publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image = image
        self.publishedAt = publishedAt


class Source:
    def __init__(self,id,name,description,url,category,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category  
        self.country = country

