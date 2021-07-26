package edu.boun.edgecloudsim.applications.sample_app7;
import edu.boun.edgecloudsim.utils.SimLogger;

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

public class QLearningAgentOld {
  Hashtable<String, List<Double>> qTable = new Hashtable<String, List<Double>>();
  double learningRate;
  double gamma;
  double epsilon;
  String qFile;
  String currentState;
  String nextState;

  List<Integer> actionSpace = Arrays.asList(0,1,2);

  public QLearningAgent(double _learningRate, double _gamma, double _epsilon, String _qFile) {
    learningRate = _learningRate;
    gamma = _gamma;
    epsilon = _epsilon;
    qFile = _qFile;
    try {
      loadQTablefromCSV();
    } catch(IOException e) {
      SimLogger.printLine("Cannot initialize agent! Terminating simulation...");
    } catch(CsvException e) {
      SimLogger.printLine("Cannot initialize agent! Terminating simulation...");
    }
	}

  public void loadQTablefromCSV() throws IOException, CsvException {
    try (CSVReader reader = new CSVReader(new FileReader(qFile))) {
        List<String[]> r = reader.readAll();
        /**if(r.size() > 0) {
            r.forEach(x -> SimLogger.printLine(x[0] + x[1] + x[2] + x[3]));
        }**/
        if(r.size() > 1) {
            r.forEach(x -> qTable.put(x[0],
                                        Arrays.asList(Double.parseDouble(x[1]),
                                                      Double.parseDouble(x[2]),
                                                      Double.parseDouble(x[3]))));
        }
    }
  }

  public void saveQTabletoCSV(){
    File file = new File(qFile);

    try {
      FileWriter outputfile = new FileWriter(file);
      CSVWriter writer = new CSVWriter(outputfile);

      List<String[]> data = new ArrayList<String[]>();
      qTable.forEach((key, value) -> data.add(new String[] { key,
                                                             String.valueOf(value.get(0)),
                                                             String.valueOf(value.get(1)),
                                                             String.valueOf(value.get(2)) }));
      writer.writeAll(data);
      writer.close();
    }
    catch (IOException e) {
      e.printStackTrace();
    }
  }
  public void addQEntry(String state){
    if(qTable.containsKey(state)){
      // do nothing
    } else {
      qTable.put(state, Arrays.asList(0.0, 0.0, 0.0));
    }
  }

  public void updateQTable(String state, String nextState, Integer action, Double reward){
    List<Double> currentQValues = new ArrayList<>();
    List<Double> nextQValues = new ArrayList<>();

    if(qTable.containsKey(state)){
      currentQValues = qTable.get(state);
    } else {
      currentQValues = Arrays.asList(0.0, 0.0, 0.0);
      qTable.put(state, currentQValues);
    }

    if(qTable.containsKey(nextState)){
      nextQValues = qTable.get(nextState);
    } else {
      nextQValues = Arrays.asList(0.0, 0.0, 0.0);
      qTable.put(nextState, nextQValues);
    }

    Double currentQValue = currentQValues.get(action);
    Double maxQValueNextState = Collections.max(nextQValues);
    Double target = learningRate * (reward + gamma* maxQValueNextState - currentQValue);
    Double updatedQValue = currentQValue + target;

    currentQValues.set(action, updatedQValue);

    qTable.put(state, currentQValues);
  }

  public int chooseAction(String state){
    List<Double> qValues = new ArrayList<>();

    if(qTable.containsKey(state)){
      qValues = qTable.get(state);
    } else {
      qValues = Arrays.asList(0.0, 0.0, 0.0);
    }
    Double maxQValue = Collections.max(qValues);
    Integer maxQValueIndex = qValues.indexOf(maxQValue);
    Double exploreProb = epsilon/actionSpace.size();
    Double maxQValueProb = 1 - epsilon + exploreProb;

    int[] actions = { 0, 1, 2 };
    double[] probability = {exploreProb, exploreProb, exploreProb};
    probability[maxQValueIndex] = maxQValueProb;

    int action = random(actions, probability);

    return action;
  }
  public static int random(int[] input, double[] probability){
      int n = input.length;
      if (n != probability.length) {
          return -1;
      }

      double[] prob_sum = new double[n];

      prob_sum[0] = probability[0];
      for (int i = 1; i < n; i++) {
          prob_sum[i] = prob_sum[i - 1] + probability[i];
      }
      Random randomizer = new Random();
      Double r = randomizer.nextDouble();

      if (r <= prob_sum[0]) {     // handle 0th index separately
          return input[0];
      }

      for (int i = 1; i < n; i++)
      {
          if (r > prob_sum[i-1] && r <= prob_sum[i]) {
              return input[i];
          }
      }

      return -1;
  }
}
