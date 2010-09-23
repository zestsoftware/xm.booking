import logging

from zope.interface import implements
from zope.annotation.interfaces import IAnnotations
from persistent.dict import PersistentDict
from interfaces import IActualHours
from interfaces import IEstimate


logger = logging.getLogger('bookings')


class ActualHoursContainer(object):
    """An adapter for actual hours containers, like Task.
    """

    implements(IActualHours)
    ANNO_KEY = 'extrememanagement.actual'

    def __init__(self, context):
        self.context = context
        annotations = IAnnotations(context)
        self.metadata = annotations.get(self.ANNO_KEY, None)
        if self.metadata is None:
            annotations[self.ANNO_KEY] = PersistentDict()
            self.metadata = annotations[self.ANNO_KEY]

    def __get_actual_time(self):
        return self.metadata.get('actual_time', 0.0)
    def __set_actual_time(self, v):
        if not isinstance(v, float):
            v = float(v)
        self.metadata['actual_time'] = v
    actual_time = property(__get_actual_time, __set_actual_time)

    def recalc(self):
        """Recalculate the total booked hours for this container.
        """
        context = self.context
        #logger.info("XXXRecalcing for %s", context)
        total = 0.0
        for obj in context.contentValues():
            #logger.info("XXXWaking up %s", obj)
            actual = IActualHours(obj, None)
            if actual is not None:
                total += actual.actual_time
        self.actual_time = total
        context.setModificationDate()
        context.reindexObject(idxs=['actual_time', 'modified',
                                    'ModificationDate'])


class EstimateContainer(ActualHoursContainer):
    implements(IEstimate)
    ANNO_KEY = 'extrememanagement.estimate'

    def __init__(self, context):
        self.context = context
        annotations = IAnnotations(context)
        self.metadata = annotations.get(self.ANNO_KEY, None)
        if self.metadata is None:
            annotations[self.ANNO_KEY] = PersistentDict()
            self.metadata = annotations[self.ANNO_KEY]

    def __get_estimate(self):
        return self.metadata.get('estimate', 0.0)
    def __set_estimate(self, v):
        if not isinstance(v, float):
            v = float(v)
        self.metadata['estimate'] = v
    estimate = property(__get_estimate, __set_estimate)

    def recalc(self):
        """Recalculate the total of estimates for this container.
        """
        context = self.context
        total = 0.0
        for obj in context.contentValues():
            adapted = IEstimate(obj, None)
            if adapted is not None:
                total += adapted.estimate
        self.estimate = total
        context.setModificationDate()
        context.reindexObject(idxs=['estimate', 'modified',
                                    'ModificationDate'])
