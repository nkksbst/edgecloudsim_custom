package edu.boun.edgecloudsim.core;

import java.util.*;

public class ExperienceBuffer {

  public List<Integer> taskIds;

  public Hashtable<Integer, Hashtable<String, String>> experiences;

  public ExperienceBuffer () {
    taskIds = new ArrayList<Integer>();
    experiences = new Hashtable<Integer, Hashtable<String, String>>();
  }
}
