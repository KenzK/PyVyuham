'''Marshal Files'''
import vyLog.vylogger

__author__ = 'Kenash K'

class vyMarshal:
    '''Marshal class for identifying the scouts to be deployed and getting the 
    reports back from the scouts
    '''
    
    def __init__(self, testsuite='Marshal_Default_Suite'):
        print 'Preparing Marshal for test execution'
        self.testsuite = testsuite
        
    def get_testcases(self):
        '''Get the tests from the suite
        '''
        pass
    
    def deploy_scouts(self):
        '''Deploy scouts for the test execution
        '''
        pass
    
    def group_scouts(self):
        '''Group scouts based on the tests to be executed
        '''
        pass
    
    def get_scout_reports(self):
        '''Get reports from the scouts based on the reports from the execution
        '''
        pass
    
    def consolidate_report(self):
        '''Consildate the reports from the scouts and consolidate for the Suite Result
        '''
        pass
    
    def execute_test(self):
        '''Start test execution
        '''
        print 'Starting test exec'
        pass