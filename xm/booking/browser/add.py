from kss.core import kssaction
from plone.app.kss.plonekssview import PloneKSSView
from Products.Five.browser import BrowserView


class Create(BrowserView):
    def __call__(self):
        form = self.request.form
        title = form.get('title', '')
        hours = form.get('hours', 0)
        minutes = form.get('minutes', 0)
        idx =1            
        while str(idx) in self.context.objectIds():
            idx = idx + 1
        self.context.invokeFactory('Booking', id=idx, title=title,
                                   hours=hours, minutes=minutes)
        self.request.response.redirect(self.context.absolute_url())


class Add(PloneKSSView):

    @kssaction
    def show_booking_form(self):
        page = self.context.restrictedTraverse('@@xm_add_booking_form')
        rendered = page()
        core = self.getCommandSet('core')
        selector = core.getHtmlIdSelector('add-booking')
        core.replaceHTML(selector, rendered)

    @kssaction
    def add_booking(self, title='test', hours=0, minutes=0):
        pass

