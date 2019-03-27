from abc import ABCMeta, abstractmethod

class Tag(object,metaclass = ABCMeta):
    # __metaclass__ = ABCMeta # python2
    def __init__(self,content='',name='',id='',hclass='',style=''):
        self.content=content
        self.name=name
        self.id=id
        self.hclass=hclass
        self.style=style

    @abstractmethod
    def display(): pass

    def __repr__(self):
        return self.display()

    __str__ = __repr__

class Div(Tag):
    def display(self):
        return '<div name="%(name)s" class="%(hclass)s" id="%(id)s" style="%(style)s">\n %(content)s\n</div>\n' % self.__dict__
   
if __name__ == "__main__": 
    div1 = Div(name="div1",content='Html stuff')
    print(div1)







