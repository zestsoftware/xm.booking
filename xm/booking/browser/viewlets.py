from plone.app.layout.viewlets import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Bookings(ViewletBase):

    render = ViewPageTemplateFile("bookingtable.pt")
