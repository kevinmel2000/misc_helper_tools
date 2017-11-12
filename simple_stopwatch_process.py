# create class for counting elapsed time for multiple process, similar with stopwatch function
# have facility to add information

import time

class StopwatchProcess:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.start_time = time.time()
        self.milestones = []
        self.summary = {}
        self.summary['start_time'] = time.time()
    
    def addMilestone(self, notes = ''):
        """
        Adds a new info to milestone. Also close if latest milestone not yet close.
        :type notes: str
        :rtype: void        
        """
        # Check latest milestone if not yet close
        if len(self.milestones) != 0 and 'end_time' not in self.milestones[-1]:
            self.closeMilestone(notes = 'close by system')
        # Every milestones is a dictionary with key info start_time, notes, etc
        new_milestone = {}
        new_milestone['start_time'] = time.time()
        new_milestone['notes'] = notes
        self.milestones.append(new_milestone)

    def closeMilestone(self, notes = ''):
        """
        Close latest milestone.
        :rtype: void        
        """
        # Check latest milestone if not yet close
        if len(self.milestones) != 0 and 'end_time' not in self.milestones[-1]:
            self.milestones[-1]['end_time'] = time.time()
            self.milestones[-1]['elapsed_time'] = self.milestones[-1]['end_time'] - self.milestones[-1]['start_time']
            self.milestones[-1]['notes'] += '-' + notes

    def summaryStopWatch(self):
        """
        Return summary of the instance of StopWatch.
        :rtype: dictionary of summary        
        """
        # Check latest milestone if not yet close
        if len(self.milestones) != 0 and 'end_time' not in self.milestones[-1]:
            self.closeMilestone(notes = 'close by system')
        # Get all key for summary
        self.summary['end_time'] = time.time()
        self.summary['total_start_end'] = self.summary['end_time'] - self.summary['start_time']
        sum_elapsed_time = 0
        for i in range(len(self.milestones)):
            sum_elapsed_time += self.milestones[i]['elapsed_time']
        self.summary['sum_milestone'] = sum_elapsed_time
        self.summary['detail_milestone'] = self.milestones
        return self.summary
