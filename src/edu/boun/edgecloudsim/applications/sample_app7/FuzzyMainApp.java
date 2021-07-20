/*
 * Title:        EdgeCloudSim - Sample Application
 *
 * Description:  Sample application for EdgeCloudSim
 *
 * Licence:      GPL - http://www.gnu.org/copyleft/gpl.html
 * Copyright (c) 2017, Bogazici University, Istanbul, Turkey
 */

package edu.boun.edgecloudsim.applications.sample_app7;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

import org.cloudbus.cloudsim.Log;
import org.cloudbus.cloudsim.core.CloudSim;

import edu.boun.edgecloudsim.core.ScenarioFactory;
import edu.boun.edgecloudsim.core.SimManager;
import edu.boun.edgecloudsim.core.SimSettings;
import edu.boun.edgecloudsim.utils.SimLogger;
import edu.boun.edgecloudsim.utils.SimUtils;

import com.opencsv.CSVReader;
import com.opencsv.CSVWriter;
import com.opencsv.exceptions.CsvException;
import java.io.IOException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.File;
import java.util.Arrays;
import java.util.Collections;
import java.lang.Math;

import java.util.*;
import java.util.Random;

public class FuzzyMainApp {

	/**
	 * Creates main() to run this example
	 */
	public static void main(String[] args) {
		String file = "/Users/monikkabusto/Desktop/src/EdgeCloudSim/data/file.csv";
		//disable console output of cloudsim library
		Log.disable();

		//enable console output and file output of this application
		SimLogger.enablePrintLog();

		int iterationNumber = 1;
		String configFile = "";
		String outputFolder = "";
		String edgeDevicesFile = "";
		String applicationsFile = "";
		if (args.length == 5){
			configFile = args[0];
			edgeDevicesFile = args[1];
			applicationsFile = args[2];
			outputFolder = args[3];
			iterationNumber = Integer.parseInt(args[4]);
		}
		else{
			SimLogger.printLine("Simulation setting file, output folder and iteration number are not provided! Using default ones...");
			configFile = "scripts/sample_app7/config/default_config.properties";
			applicationsFile = "scripts/sample_app7/config/applications.xml";
			edgeDevicesFile = "scripts/sample_app7/config/edge_devices.xml";
			outputFolder = "sim_results/ite" + iterationNumber;
		}

		//load settings from configuration file
		SimSettings SS = SimSettings.getInstance();
		if(SS.initialize(configFile, edgeDevicesFile, applicationsFile) == false){
			SimLogger.printLine("cannot initialize simulation settings!");
			System.exit(0);
		}

		if(SS.getFileLoggingEnabled()){
			SimLogger.enableFileLog();
			SimUtils.cleanOutputFolder(outputFolder);
		}

		DateFormat df = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
		Date SimulationStartDate = Calendar.getInstance().getTime();
		String now = df.format(SimulationStartDate);
		SimLogger.printLine("Simulation started at " + now);
		SimLogger.printLine("----------------------------------------------------------------------");

		for(int j=SS.getMinNumOfMobileDev(); j<=SS.getMaxNumOfMobileDev(); j+=SS.getMobileDevCounterSize())
		{
			for(int k=0; k<SS.getSimulationScenarios().length; k++) // TWO_TIER_WITH_EO
			{
				for(int i=0; i<SS.getOrchestratorPolicies().length; i++) // Q_LEARNING
				{
					String simScenario = SS.getSimulationScenarios()[k];
					String orchestratorPolicy = SS.getOrchestratorPolicies()[i];
					Date ScenarioStartDate = Calendar.getInstance().getTime();
					now = df.format(ScenarioStartDate);

					SimLogger.printLine("Scenario started at " + now);
					SimLogger.printLine("Scenario: " + simScenario + " - Policy: " + orchestratorPolicy + " - #iteration: " + iterationNumber);
					SimLogger.printLine("Duration: " + SS.getSimulationTime()/60 + " min (warm up period: "+ SS.getWarmUpPeriod()/60 +" min) - #devices: " + j);
					SimLogger.getInstance().simStarted(outputFolder,"SIMRESULT_" + simScenario + "_"  + orchestratorPolicy + "_" + j + "DEVICES");

					try
					{
						// First step: Initialize the CloudSim package. It should be called
						// before creating any entities.
						int num_user = 2;   // number of grid users
						Calendar calendar = Calendar.getInstance();
						boolean trace_flag = false;  // mean trace events

						// Initialize the CloudSim library
						CloudSim.init(num_user, calendar, trace_flag, 0.01);

						// Generate EdgeCloudsim Scenario Factory
						ScenarioFactory sampleFactory = new FuzzyScenarioFactory(j,SS.getSimulationTime(), orchestratorPolicy, simScenario);

						// Generate EdgeCloudSim Simulation Manager
						SimManager manager = new SimManager(sampleFactory, j, simScenario, orchestratorPolicy);

						// Start simulation
						manager.startSimulation();
						appendSimulationDivider(file, j);
					}
					catch (Exception e)
					{
						SimLogger.printLine("The simulation has been terminated due to an unexpected error");
						e.printStackTrace();
						System.exit(0);
					}

					Date ScenarioEndDate = Calendar.getInstance().getTime();
					now = df.format(ScenarioEndDate);
					SimLogger.printLine("Scenario finished at " + now +  ". It took " + SimUtils.getTimeDifference(ScenarioStartDate,ScenarioEndDate));
					SimLogger.printLine("----------------------------------------------------------------------");
				}//End of orchestrators loop
			}//End of scenarios loop
		}//End of mobile devices loop

		Date SimulationEndDate = Calendar.getInstance().getTime();
		now = df.format(SimulationEndDate);
		SimLogger.printLine("Simulation finished at " + now +  ". It took " + SimUtils.getTimeDifference(SimulationStartDate,SimulationEndDate));
	}
	public static void appendSimulationDivider(String file, int numDevices) throws IOException, CsvException {
	  try {
	      CSVReader reader = new CSVReader(new FileReader(file));

	      Hashtable<String, List<Double>> qTable = new Hashtable<String, List<Double>>();
	      List<String[]> r = reader.readAll();
	      if(r.size() > 0) {
	          r.forEach(x -> qTable.put(x[0],
	                                      Arrays.asList(Double.parseDouble(x[1]),
	                                                    Double.parseDouble(x[2]),
	                                                    Double.parseDouble(x[3]))));
	      }
	      qTable.put("DEVICES" + String.valueOf(numDevices), Arrays.asList(0.0, 0.0,0.0));

	      CSVWriter writer = new CSVWriter(new FileWriter(file));
	      List<String[]> data = new ArrayList<String[]>();
	      qTable.forEach((key, value) -> data.add(new String[] { key,
	                                                             String.valueOf(value.get(0)),
	                                                             String.valueOf(value.get(1)),
	                                                             String.valueOf(value.get(2)) }));
	      writer.writeAll(data);
	      writer.close();
	  } catch(IOException e) {
				SimLogger.printLine("Error adding device divider");
				e.printStackTrace();
				System.exit(0);
		} catch(CsvException e){
			SimLogger.printLine("Error adding device divider");
			e.printStackTrace();
			System.exit(0);
		}
	}
}
