c1241de048480265da66ab48a760acda0c022d18
diff --git a/exec_vyuham.py b/exec_vyuham.py
new file mode 100644
index 0000000000000000000000000000000000000000..2471cba2da0af9dc6549e0d5ab237fcc38c8047e
--- /dev/null
+++ b/exec_vyuham.py
@@ -0,0 +1,68 @@
+#!/usr/bin/env python
+
+import sys
+import os
+import argparse
+
+import vyUtils.vyMarshal as Marshal
+import vyUtils.vyScout as Scout
+
+class VyuhamExec:
+    '''
+     VyuhamExec is the main class that would be triggering the Marshal to deploy scouts
+    for execution.
+    This would identify if the tests are repositories of the testcases.
+    '''
+    
+    def __init__(self):
+        """
+
+        self.result
+
+        """
+        self.result = {'Pass':True, 'Fail':False, 'Abort':''}
+        self.repo = {}
+        self.testtype = []
+        self.loadplugin = []
+        
+        
+#    def m_argparser(self, *m_args, **m_kwargs):
+    def m_argparser(self):
+        """
+        Parses the Marshal arguments and validate
+            Arguments:
+                m_args:
+                m_kwargs:
+            Returns:
+                if valid:
+                    return True
+                else:
+                    Display Help
+                    return False
+        """
+        m_parser = argparse.ArgumentParser(description="PyVyuham Exec Options")
+        m_parser.add_argument("scriptpath", metavar = 'TC', type=str,
+                              nargs = '+', help="Test script Name/ Location")
+        m_parser.add_argument("-c", "--config", help="Marshal config file",
+                              type=str)
+        m_parser.add_argument("-v", "--verbose", default=1,
+                              action = "store_true", help="Set logging level")
+        m_parser.add_argument("-q", "--quiet", action = "store_true",
+                              help="Set quiet exec mode")
+        m_parser.parse_args()
+
+        return m_parser
+
+    def main(self, *args):
+        print "Test Marshal"
+
+if __name__ == "__main__":
+    vyuham = VyuhamExec()
+#    m_args = marshal_obj.m_argparser(sys.argv)
+    m_args = vyuham.m_argparser()
+    if m_args:
+        vyuham.main(m_args)
+    else:
+        print "Invalid Args"
+
+
diff --git a/marshal.py b/marshal.py
deleted file mode 100644
index b947b53032356d5624304b0411aa9a68de0bec29..0000000000000000000000000000000000000000
--- a/marshal.py
+++ /dev/null
@@ -1,63 +0,0 @@
-#!/usr/bin/env python
-
-import sys
-import os
-import argparse
-
-class Marshal:
-    """
-    Marshal is the main class that would be triggering the scouts for execution.
-    This would identify if the tests are repositories of the testcases.
-    """
-    def __init__(self):
-        """
-
-        self.result
-
-        """
-        self.result = {'Pass':True, 'Fail':False, 'Abort':''}
-        self.repo = {}
-        self.testtype = []
-        self.loadplugin = []
-        
-        
-#    def m_argparser(self, *m_args, **m_kwargs):
-    def m_argparser(self):
-        """
-        Parses the Marshal arguments and validate
-            Arguments:
-                m_args:
-                m_kwargs:
-            Returns:
-                if valid:
-                    return True
-                else:
-                    Display Help
-                    return False
-        """
-        m_parser = argparse.ArgumentParser(description="PyVyuham Exec Options")
-        m_parser.add_argument("-t", "--testscript", type=str,
-                              help="Test script filename")
-        m_parser.add_argument("-c", "--config", help="Marshal config file",
-                              type=str)
-        m_parser.add_argument("-v", "--verbose", default=1,
-                              action = "store_true", help="Set logging level")
-        m_parser.add_argument("-q", "--quiet", action = "store_true",
-                              help="Set quiet exec mode")
-        m_parser.parse_args()
-
-        return m_parser
-
-    def main(self, *args):
-        print "Test Marshal"
-
-if __name__ == "__main__":
-    marshal_obj = Marshal()
-#    m_args = marshal_obj.m_argparser(sys.argv)
-    m_args = marshal_obj.m_argparser()
-    if m_args.testscript:
-        marshal_obj.main(m_args)
-    else:
-        print m_args.print_help()
-
-
diff --git a/tests/env.py b/tests/env.py
new file mode 100644
index 0000000000000000000000000000000000000000..2bd74bcd402ec8c8cb7f0007ff191e6b0e6288cd
--- /dev/null
+++ b/tests/env.py
@@ -0,0 +1,2 @@
+'''Setup the test env for unit testing PyVyuham'''
+__author__ = 'Kenash K'
\ No newline at end of file
diff --git a/vyConfig/init_config.ini b/vyConfig/init_config.ini
index d74606b909dabf3ef97fdd5c1745525774f9c105..d1a2c2b5b93ff48e12a5109b828a49eef9c1c02a 100644
--- a/vyConfig/init_config.ini
+++ b/vyConfig/init_config.ini
@@ -1,10 +1,16 @@
 [Project]
-Name="Test"
+Name="Test_Run"
 Repo=""
 Owner="Who Knows"
 Version="v1.0"
 
 [Suite]
+Name="TestRunSuite"
+File="TR_Suite1"
 
-
-[Testcase]
\ No newline at end of file
+[Testcase]
+Root="./sample_tests/"
+Test1="TC1.py"
+Test2="TC2.py"
+Test3="TC3.py"
+Test4="TC4.py"
\ No newline at end of file
diff --git a/vyFramework/vyMain.py b/vyFramework/vyMain.py
index a1ced0bd0f2948c8774caf7be82fa934d41a0cac..111227bbf39a3b4c309cde5e89d467ae3e6d8d58 100644
--- a/vyFramework/vyMain.py
+++ b/vyFramework/vyMain.py
@@ -1,12 +1,19 @@
 #Main object class for the Framework
-import vylogger
+import vyLog
 
-import vyUtils.vymarshal as vymarshal
-import vyUtils.vyscout as vyscout
+import vyUtils.vyMarshal as vymarshal
+import vyUtils.vyScout as vyscout
 
 class vyMain:
     def __init__(self):
         """Build PyVyuham
         """
-        self.scout=vyscout()
-        self.marshal=vymarshal()
\ No newline at end of file
+        print vyLog
+        print vymarshal
+        print vyscout
+        ##self.marshal=vymarshal()
+        
+    def launch_execution(self):
+        '''Launch Vyuham'''
+        pass
+    
\ No newline at end of file
diff --git a/vyLog/__init__.py b/vyLog/__init__.py
new file mode 100644
index 0000000000000000000000000000000000000000..c32ade97c1a25475e1752b7924d106de3b901d74
--- /dev/null
+++ b/vyLog/__init__.py
@@ -0,0 +1 @@
+'''Logger package'''
\ No newline at end of file
diff --git a/vyRepo/scripts/demo_script1.py b/vyRepo/scripts/demo_script1.py
deleted file mode 100644
index e3d7c5b54eb311bce83cc81435229252bd77000f..0000000000000000000000000000000000000000
--- a/vyRepo/scripts/demo_script1.py
+++ /dev/null
@@ -1,8 +0,0 @@
-#Demo python script
-import vyFramework.vyTest as vyTest
-
-class test_demo(vyMain):
-    """
-    Demo test class
-    """
-    
\ No newline at end of file
diff --git a/vyRepo/scripts/demo_script2.py b/vyRepo/scripts/demo_script2.py
deleted file mode 100644
index ce6e9ea1e0187b793b09a8721302dbbcaf7e7bcc..0000000000000000000000000000000000000000
--- a/vyRepo/scripts/demo_script2.py
+++ /dev/null
@@ -1 +0,0 @@
-#Demo script2
\ No newline at end of file
diff --git a/vyTestRepo/scripts/demo_script1.py b/vyTestRepo/scripts/demo_script1.py
new file mode 100644
index 0000000000000000000000000000000000000000..e3d7c5b54eb311bce83cc81435229252bd77000f
--- /dev/null
+++ b/vyTestRepo/scripts/demo_script1.py
@@ -0,0 +1,8 @@
+#Demo python script
+import vyFramework.vyTest as vyTest
+
+class test_demo(vyMain):
+    """
+    Demo test class
+    """
+    
\ No newline at end of file
diff --git a/vyTestRepo/scripts/demo_script2.py b/vyTestRepo/scripts/demo_script2.py
new file mode 100644
index 0000000000000000000000000000000000000000..ce6e9ea1e0187b793b09a8721302dbbcaf7e7bcc
--- /dev/null
+++ b/vyTestRepo/scripts/demo_script2.py
@@ -0,0 +1 @@
+#Demo script2
\ No newline at end of file
diff --git a/vyUtils/vyMarshal/__init__.py b/vyUtils/vyMarshal/__init__.py
new file mode 100644
index 0000000000000000000000000000000000000000..e69de29bb2d1d6434b8b29ae775ad8c2e48c5391
diff --git a/vyUtils/vyMarshal/readme b/vyUtils/vyMarshal/readme
new file mode 100644
index 0000000000000000000000000000000000000000..f61bc2766b5ef2fcde313c66cdff7459965ed77d
--- /dev/null
+++ b/vyUtils/vyMarshal/readme
@@ -0,0 +1 @@
+***This is the vymarshal lib***
\ No newline at end of file
diff --git a/vyUtils/vyMarshal/vymarshal.py b/vyUtils/vyMarshal/vymarshal.py
new file mode 100644
index 0000000000000000000000000000000000000000..a20063990d0bb65121f618d1669740456461b2c1
--- /dev/null
+++ b/vyUtils/vyMarshal/vymarshal.py
@@ -0,0 +1,37 @@
+'''Marshal Files'''
+__author__ = 'Kenash K'
+
+class vyMarshal:
+    '''Marshal class for identifying the scouts to be deployed and getting the 
+    reports back from the scouts
+    '''
+    
+    def __init__(self, testsuite):
+        self.testsuite = testsuite
+        
+    def get_testcases(self):
+        '''Get the tests from the suite
+        '''
+        pass
+    
+    def deploy_scouts(self):
+        '''Deploy scouts for the test execution
+        '''
+        pass
+    
+    def group_scouts(self):
+        '''Group scouts based on the tests to be executed
+        '''
+        pass
+    
+    def get_scout_reports(self):
+        '''Get reports from the scouts based on the reports from the execution
+        '''
+        pass
+    
+    def consolidate_report(self):
+        '''Consildate the reports from the scouts and consolidate for the Suite Result
+        '''
+        pass
+    
+    
\ No newline at end of file
diff --git a/vyUtils/vyScout/__init__.py b/vyUtils/vyScout/__init__.py
new file mode 100644
index 0000000000000000000000000000000000000000..e69de29bb2d1d6434b8b29ae775ad8c2e48c5391
diff --git a/vyUtils/vyScout/readme b/vyUtils/vyScout/readme
new file mode 100644
index 0000000000000000000000000000000000000000..e8bcd265cb9e55c49b9546b26e2d2cc1b9c58010
--- /dev/null
+++ b/vyUtils/vyScout/readme
@@ -0,0 +1 @@
+***This is the Scout lib. This support the Scout utility for running and monitoring the testcases***
\ No newline at end of file
diff --git a/vyUtils/vymarshal/__init__.py b/vyUtils/vymarshal/__init__.py
deleted file mode 100644
index e69de29bb2d1d6434b8b29ae775ad8c2e48c5391..0000000000000000000000000000000000000000
diff --git a/vyUtils/vymarshal/readme b/vyUtils/vymarshal/readme
deleted file mode 100644
index f61bc2766b5ef2fcde313c66cdff7459965ed77d..0000000000000000000000000000000000000000
--- a/vyUtils/vymarshal/readme
+++ /dev/null
@@ -1 +0,0 @@
-***This is the vymarshal lib***
\ No newline at end of file
diff --git a/vyUtils/vyscout/__init__.py b/vyUtils/vyscout/__init__.py
deleted file mode 100644
index e69de29bb2d1d6434b8b29ae775ad8c2e48c5391..0000000000000000000000000000000000000000
diff --git a/vyUtils/vyscout/readme b/vyUtils/vyscout/readme
deleted file mode 100644
index e8bcd265cb9e55c49b9546b26e2d2cc1b9c58010..0000000000000000000000000000000000000000
--- a/vyUtils/vyscout/readme
+++ /dev/null
@@ -1 +0,0 @@
-***This is the Scout lib. This support the Scout utility for running and monitoring the testcases***
\ No newline at end of file
