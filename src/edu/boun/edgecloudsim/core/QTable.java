package edu.boun.edgecloudsim.core;

import java.util.*;

public class QTable {

  public Hashtable<String, List<Double>> table;
  Double gamma;
  Double learningRate;

  public QTable (Double _gamma, Double _learningRate) {
    table = new Hashtable<String, List<Double>>();
    gamma = _gamma;
    learningRate = _learningRate;
  }

  public void updateTable(Hashtable<String, String> experience){
    String currentState = experience.get("currentState");
    String nextState = experience.get("nextState");
    Integer action = Integer.valueOf(experience.get("action"));
    Double reward = experience.get("status").equals("completed") ? 1.0 : -1.0;

    if(!table.containsKey(currentState))
    {
      table.put(currentState, Arrays.asList(0.0, 0.0, 0.0));
    }
    if(!table.containsKey(nextState))
    {
      table.put(nextState, Arrays.asList(0.0, 0.0, 0.0));
    }

    Double currentQValue = table.get(currentState).get(action);
    Double maxQValueNextState = Collections.max(table.get(nextState));
    Double target = learningRate * (reward + gamma* maxQValueNextState - currentQValue);
    Double updatedQValue = currentQValue + target;

    table.get(currentState).set(action, updatedQValue);
  }

  public Hashtable<String, List<Double>> getTable() {
    return table;
  }

  public void addData(String simulationIndex) {
    table.put(simulationIndex, Arrays.asList(0.0, 0.0, 0.0));
  }


}
