from kss.core import kssaction
from plone.app.kss.plonekssview import PloneKSSView


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

