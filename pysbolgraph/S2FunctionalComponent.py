
from S2Identified import S2Identified

from terms import SBOL2

class S2FunctionalComponent(S2Identified):
    def __init__(self, g, uri):
        super(S2FunctionalComponent, self).__init__(g, uri)

    @property
    def definition(self):
        return self.getIdentifiedProperty(SBOL2.definition)
    @definition.setter
    def definition(self, definition):
        self.setIdentifiedProperty(SBOL2.definition, definition)

    @property
    def access(self):
        return self.getUriProperty(SBOL2.access)
    @access.setter
    def access(self, access):
        self.setUriProperty(SBOL2.access, access)

    @property
    def direction(self):
        return self.getUriProperty(SBOL2.direction)
    @direction.setter
    def direction(self, direction):
        self.setUriProperty(SBOL2.direction, direction)


