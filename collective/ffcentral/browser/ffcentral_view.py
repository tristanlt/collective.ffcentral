from zope import interface
from Products.Five.browser import BrowserView

class ffcentralPage(BrowserView):
    def update(self):
        self.fffolders = self.context.listFolderContents(contentFilter={"portal_type" : "FeedfeederFolder"})
        return self.fffolders
