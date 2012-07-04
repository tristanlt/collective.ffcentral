from zope import interface
from Products.Five.browser import BrowserView

class ffcentralPage(BrowserView):
    def update(self):
        self.output=[]
        
        self.fffolders = self.context.listFolderContents(contentFilter={"portal_type" : "FeedfeederFolder"})
        
        for self.fffolder in self.fffolders:
            self.fffinfo={'title':self.fffolder.title,'desc':self.fffolder.Description,'url':self.fffolder.absolute_url}
            listing=self.fffolder.getFolderContents
            self.ffitems = listing({'sort_on': 'getFeedItemUpdated','sort_order': 'descending','portal_type': 'FeedFeederItem'})
            self.ffi=[]
            for index, self.ffitem in enumerate(self.ffitems[0:10]):
                self.ffi.append({'title':self.ffitem.Title,'desc':self.ffitem.Description,'url':self.ffitem.getURL(),'date':self.ffitem.getFeedItemUpdated})
            self.fffinfo['ffitems']=self.ffi
            self.output.append(self.fffinfo)
        return self.output