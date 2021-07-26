package edu.boun.edgecloudsim.applications.sample_app7;

import edu.boun.edgecloudsim.utils.SimLogger;
import edu.boun.edgecloudsim.core.QTable;

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

public class QLearningAgent {
  List<Integer> actionSpace;
  Double epsilon;

  public QLearningAgent() {
    actionSpace = Arrays.asList(0,1,2);
    epsilon = 0.85;
	}

  public int chooseAction(Hashtable<String, List<Double>> qTable, String state){
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

  private static int random(int[] input, double[] probability){
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
