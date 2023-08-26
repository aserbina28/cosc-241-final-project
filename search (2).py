# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    start_state = problem.getStartState()
    curr_node = [start_state, [], 0]
    # curr_node is a node,
    # curr_node[0] is the position or state
    # curr_node[1] is a list that contains path
    # curr_node[2] is the cost of the path

    frontier = util.Stack()
    frontier.push(curr_node)
    explored = set()
    print("Here")
    while not frontier.isEmpty() :
        curr_node = frontier.pop()
        if problem.isGoalState(curr_node[0]) :
            print("Path found:", curr_node[1])
            return curr_node[1]

        if not curr_node[0] in explored:
            explored.add(curr_node[0])
            curr_successors = problem.getSuccessors(curr_node[0])
            #curr_successors holds a list of triples
            #one_successor holds (successor, action, stepCost)
            for one_successor in curr_successors:
                successor_state, action, stepCost = one_successor
                new_successor_node = [successor_state, curr_node[1]+[action], curr_node[2] + stepCost]
                frontier.push(new_successor_node)
    print("Returning no path found")
    return [];



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    start_state = problem.getStartState()
    curr_node = [start_state, [], 0]
    # curr_node is a node,
    # curr_node[0] is the position or state
    # curr_node[1] is a list that contains path
    # curr_node[2] is the cost of the path

    frontier = util.Queue()
    frontier.push(curr_node)
    explored = set()
    print("Here")
    while not frontier.isEmpty():
        curr_node = frontier.pop()
        if problem.isGoalState(curr_node[0]):
            print("Path found:", curr_node[1])
            return curr_node[1]

        if not curr_node[0] in explored:
            explored.add(curr_node[0])
            curr_successors = problem.getSuccessors(curr_node[0])
            # curr_successors holds a list of triples
            # one_successor holds (successor, action, stepCost)
            for one_successor in curr_successors:
                successor_state, action, stepCost = one_successor
                new_successor_node = [successor_state, curr_node[1] + [action], curr_node[2] + stepCost]
                frontier.push(new_successor_node)
    print("Returning no path found")
    return [];

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    start_state = problem.getStartState()
    curr_node = [start_state, [], 0]
    # curr_node is a node,
    # curr_node[0] is the position or state
    # curr_node[1] is a list that contains path
    # curr_node[2] is the cost of the path

    frontier = util.PriorityQueue()
    frontier.push(curr_node, 0)
    explored = set()

    while not frontier.isEmpty():
        curr_node = frontier.pop()
        if problem.isGoalState(curr_node[0]):
            #print("Path found:", curr_node[1])
            return curr_node[1]

        if not curr_node[0] in explored:
            explored.add(curr_node[0])
            curr_successors = problem.getSuccessors(curr_node[0])
            # curr_successors holds a list of triples
            # one_successor holds (successor, action, stepCost)
            for one_successor in curr_successors:
                successor_state, action, stepCost = one_successor
                new_successor_node = [successor_state, curr_node[1] + [action], curr_node[2] + stepCost]
                frontier.push(new_successor_node, new_successor_node[2])
    print("Returning no path found")
    return [];

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    start_state = problem.getStartState()
    curr_node = [start_state, [], 0]
    # curr_node is a node,
    # curr_node[0] is the position or state
    # curr_node[1] is a list that contains path
    # curr_node[2] is the cost of the path

    frontier = util.PriorityQueue()
    frontier.push(curr_node, 0 + heuristic(curr_node[0], problem))
    explored = set()

    while not frontier.isEmpty():
        curr_node = frontier.pop()
        if problem.isGoalState(curr_node[0]):
            return curr_node[1]

        if not curr_node[0] in explored:
            explored.add(curr_node[0])
            curr_successors = problem.getSuccessors(curr_node[0])
            # curr_successors holds a list of triples
            # one_successor holds (successor, action, stepCost)
            for one_successor in curr_successors:
                successor_state, action, stepCost = one_successor
                new_successor_node = [successor_state, curr_node[1] + [action], curr_node[2] + stepCost]
                frontier.push(new_successor_node, new_successor_node[2] + heuristic(new_successor_node[0], problem))
    return [];


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
