# Library for building correct TCX file
from lxml import etree

class TCXBuilder(object):
    HEADER = """
<TrainingCenterDatabase xmlns="http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2" 
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
  xsi:schemaLocation="http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2 http://www.garmin.com/xmlschemas/TrainingCenterDatabasev2.xsd">
</TrainingCenterDatabase>
"""
    NS = '{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}'

    ACTIVITIES = [ "Other", "Running", "Biking", "MultiSport", "Other"]

    def __init__(self):
        self.root = None
        self.ready = False

    def new(self, sport="Other", start_time="2014-04-23T19:26:31Z"):
        self.root = etree.fromstring(self.HEADER)
        self.doc = etree.ElementTree(self.root)
        if not sport in self.ACTIVITIES:
            sport = self.ACTIVITIES[0]

        activities = etree.SubElement(self.root, "Activities")
        activity = etree.SubElement(activities, "Activity", Sport=sport)

        id_tag = etree.SubElement(activity, "Id")

        lap_tag = etree.SubElement(activity, "Lap", StartTime=start_time)
        lap_tag.text = "Empty"

    def setId(self, newId):
        id_tag = self.root.xpath('Activities/Activity/Id')[0]
        id_tag.text = newId

    def out(self):
        return etree.tostring(self.root)

