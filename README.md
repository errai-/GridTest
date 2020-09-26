It is assumed that the file vomx.proxy is provided in the home directory.
This is achieved by running a command of the sort:
 * voms-proxy-init -voms cms -valid 192:00
 * cp /tmp/x509up_uREPLACETHIS $HOME/voms.proxy

Create a working area:
 * scram p -n TEST10616 CMSSW CMSSW_10_6_16
 * cd TEST10616/src

Clone this repo:
 * git clone git@github.com:errai-/GridTest.git

Configure CMSSW and build:
 * cmsenv
 * scram b -j

Go to the working directory and perform a test run:
 * cd GridTest/Test/python
 * cmsRun runner.py

If everything was ok, change the following in the grid-control.conf file:

 * workdir (change this to some available directory)
 * X509_USER_PROXY (set this to match the home directory)
 * se path (this needs to be a grid location available to the tester)
 * project area (this needs to point to the current CMSSW location)

Now, the only thing left is to run grid-control:

 * grid-control grid-control.conf

The bug that is being observed is that most jobs seem to fail (some pass).
In reality, most of the jobs have passed, but somehow the communication between the SE and the running node fails.
The running node receives most likely a message of failure and consequently of success - but will think that the job failed.
The issue coul be about the SE, but also very likely about the running nodes.

The dummy analysis that this test presents simply looks at a (MC) dataset and saves some info about the PF candidates.
This analysis could be run on any dataset, but here it is pointed at some ttbar samples.
