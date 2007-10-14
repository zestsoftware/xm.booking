from kss.core import kssaction
from plone.app.kss.plonekssview import PloneKSSView
from Products.Five.browser import BrowserView
from viewlets import Bookings as BookingsViewlet
from viewlets import BookingForm as BookingFormViewlet


def create_booking(context, title='test 2', hours=0, minutes=0):
    idx = 1
    while str(idx) in context.objectIds():
        idx = idx + 1
    context.invokeFactory('Booking', id=idx, title=title,
                          hours=hours, minutes=minutes)


class Create(BrowserView):
    def __call__(self):
        form = self.request.form
        title = form.get('title', '')
        hours = form.get('hours', 0)
        minutes = form.get('minutes', 0)
        create_booking(self.context, title=title, hours=hours, minutes=minutes)
        self.request.response.redirect(self.context.absolute_url())


class Add(PloneKSSView):

    @kssaction
    def add_booking(self, data):
        create_booking(self.context, title=data.title,
                       hours=data.hours, minutes=data.minutes)
        core = self.getCommandSet('core')

        # Refresh the booking table
        viewlet = BookingsViewlet(self.context, self.request, None, None)
        viewlet.update()
        rendered = viewlet.render()
        selector = core.getHtmlIdSelector('booking-table')
        core.replaceHTML(selector, rendered)

        # Refresh the add booking form
        viewlet = BookingFormViewlet(self.context, self.request, None, None)
        viewlet.update()
        rendered = viewlet.render()
        selector = core.getHtmlIdSelector('add-booking')
        core.replaceHTML(selector, rendered)

