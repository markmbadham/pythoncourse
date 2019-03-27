import xml.sax,re

class AlbumHandler(xml.sax.ContentHandler):
    def startDocument(self):
        print("starting document \n")
        self.artists = {}
        self.lastartist=''
        self.currentTag=''
        self.found = False

    def startElement(self,tag,attributes):
        print("found element %s \n" % tag, dict(attributes))
        self.currentTag = tag
        if tag == 'album':
            self.artists[self.lastartist].append(attributes.get('id'))

    def characters(self,data):
        if not re.search('^\s*$',data):
            print("found data : %s \n" % data)
            if self.currentTag == 'artist':
                self.artists[data] = []
                self.lastartist = data

    def endDocument(self):
       print(self.artists.__repr__())

xml.sax.parse("http://leadingtraining.co.za/album.xml",AlbumHandler())
