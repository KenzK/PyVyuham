#!/usr/bin/env python

import sys
import os
import argparse

class Marshal:
    """
    Marshal is the main class that would be triggering the scouts for execution.
    This would identify if the tests are repositories of the testcases.
    """
    def __init__(self):
        """

        self.result

        """
        self.result = {'Pass':True, 'Fail':False, 'Abort':''}
        self.repo = {}
        self.testtype = []
        self.loadplugin = []

#    def m_argparser(self, *m_args, **m_kwargs):
    def m_argparser(self):
        """
        Parses the Marshal arguments and validate
            Arguments:
                m_args:
                m_kwargs:
            Returns:
                if valid:
                    return True
                else:
                    Display Help
                    return False
        """
        m_parser = argparse.ArgumentParser(description="PyVyuham Exec Options")
        m_parser.add_argument("-t", "--testscript", type=str,
                              help="Test script filename")
        m_parser.add_argument("-c", "--config", help="Marshal config file",
                              type=str)
        m_parser.add_argument("-v", "--verbose", default=1,
                              action = "store_true", help="Set logging level")
        m_parser.add_argument("-q", "--quiet", action = "store_true",
                              help="Set quiet exec mode")
        m_parser.parse_args()

        return m_parser

    def main(self, *args):
        print "Test Marshal"

if __name__ == "__main__":
    marshal_obj = Marshal()
#    m_args = marshal_obj.m_argparser(sys.argv)
    m_args = marshal_obj.m_argparser()
    if m_args.testscript:
        marshal_obj.main(m_args)
    else:
        print m_args.print_help()


