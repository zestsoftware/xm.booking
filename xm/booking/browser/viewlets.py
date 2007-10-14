from plone.app.layout.viewlets import ViewletBase
#from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Bookings(ViewletBase):

    #render = ViewPageTemplateFile("document_actions.pt")
    def render(self):
        return "Hi there!"
