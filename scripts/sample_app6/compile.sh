#!/bin/sh
rm -rf ../../bin
mkdir ../../bin
javac -classpath "../../lib/cloudsim-4.0.jar:../../lib/commons-math3-3.6.1.jar:../../lib/jFuzzyLogic_v3.0.jar:../../lib/colt.jar:../../lib/opencsv-5.5.jar:../../lib/jtransc-rt-core-0.6.8.jar:../../lib/commons-lang3-3.12.0.jar" -sourcepath ../../src ../../src/edu/boun/edgecloudsim/applications/sample_app6/FuzzyMainApp.java -d ../../bin
