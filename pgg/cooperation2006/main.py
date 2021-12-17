import random as rd
import numpy as np
import matplotlib.pyplot as plt

n_of_groups = 5
n_of_agents = n_of_groups * 100
n_of_rounds = 100
mult_factor = 1.01

def initialize_game():
    agents = list()
    groups = list()
    sizes = []
    
    # Create the new agents 
    # and populates the list of agents
    for i in range(n_of_agents):
        new_cooperation = rd.choice([0,1])
        new_agent = dict(cooperation = new_cooperation)
        agents.append(new_agent)

    # Creates the list of groups
    for i in range(n_of_groups):
        new_group = dict(agents_pos = list(), size = 0, wealth = 0)
        groups.append(new_group)

    # Assigns a group to each agent 
    for agent in agents:
        group_new = rd.choice(groups)
        group_new["agents_pos"].append(agents.index(agent))
        group_new["size"] = group_new["size"] + 1 

        agent["group_pos"] = groups.index(group_new)

    # Initializes sizes 
    for g in range(len(groups)):
        sizes.append([])

    for g in range(len(groups)):
        sizes[g].append(groups[g]["size"])

    return agents, groups, sizes

def play_game(agents, groups, sizes):

    # Compute the groups' wealths
    for group in groups:
        group["wealth"] = 0
        for agent_pos in group["agents_pos"]:
            group["wealth"] = group["wealth"] + mult_factor*agents[agent_pos]["cooperation"]

    # Compute the individual weights 

    weights = list()

    for agent in agents:
        agent["weight"] = agent["cooperation"] + groups[agent["group_pos"]]["wealth"]/groups[agent["group_pos"]]["size"]
        weights.append(agent["weight"])


    # Create the new agents
    new_set_of_agents = list()

    for i in range(n_of_agents):
        parent = rd.choices(agents, weights, k = 1)[0]
        new_agent = dict(cooperation = parent["cooperation"], group_pos = parent["group_pos"])
        new_set_of_agents.append(new_agent)


    # Create the new groups
    new_groups = list()
    for g in range(n_of_groups):
        new_groups.append(dict(agents_pos = list(), size = 0))
    
    # Assign the new agents to the new groups
    for i in range(len(new_set_of_agents)):
        agent = new_set_of_agents[i]
        group = new_groups[agent["group_pos"]]
        group["agents_pos"].append(i)
        group["size"] = group["size"] + 1 

    new_sizes = sizes[:]
    for g in range(n_of_groups):
        new_sizes[g].append(new_groups[g]["size"])


    return(new_set_of_agents, new_groups, new_sizes)





agents, groups, sizes = initialize_game()
for i in range(n_of_rounds):
    agents, groups, sizes = play_game(agents, groups, sizes)

t = np.linspace(1, n_of_rounds+1, num =  n_of_rounds + 1)
for g in range(n_of_groups):
    plt.plot(t,sizes[g])
plt.show()




























""" agents = list()
groups = list()
sizes = [] """


""" 
Starts the game. 

Populates the list of agents, with new agents 
whose cooperation levels are either 0 or 1, chosen at random.

Assigns a group to each new agent. 
"""

""" 
def initialize_game():

    agents = list()
    groups = list()
    sizes = []
    
    # Create the new agents 
    # and populates the list of agents
    for i in range(n_of_agents):
        new_cooperation = rd.choice([0,1])
        new_agent = dict(cooperation = new_cooperation)
        agents.append(new_agent)

    # Creates the list of groups
    for i in range(n_of_groups):
        new_group = dict(agents_pos = list(), size = 0, wealth = 0)
        groups.append(new_group)

    # Assigns a group to each agent 
    for agent in agents:
        group_new = rd.choice(groups)
        assign_group(agent, group_new)

    return agents, groups, sizes

def assign_group(agent, group):
    group["agents_pos"].append(agents.index(agent))
    group["size"] = group["size"] + 1 

    agent["group"] = groups.index(group)



def play_game():
    update_wealth()
    create_new_generation(agents)
    update_sizes()

def update_wealth():
    for group in groups:
        group["wealth"] = 0
        for agent_pos in group["agents_pos"]:
            group["wealth"] = group["wealth"] + mult_factor*agents[agent_pos]["cooperation"]

def create_new_generation(agents):
    weights = list()

    for agent in agents:
        agent["weight"] = agent["cooperation"] + groups[agent["group"]]["wealth"]/groups[agent["group"]]["size"]
        weights.append(agent["weight"])

    new_set_of_agents = list()

    for i in range(n_of_agents):
        parent = rd.choices(agents, weights, k = 1)[0]
        new_agent = dict(cooperation = parent["cooperation"], group = parent["group"])
        new_set_of_agents.append(new_agent)

    for agent in new_set_of_agents:
        assign_group(agent, groups[agent["group"]])

    return(new_set_of_agents)

def update_sizes():
    for g in range(len(groups)):
        sizes[g].append(groups[g]["size"])







# playing the game and plotting the results

initialize_game()

for round in range(n_of_rounds):
    play_game()

t = np.linspace(n_of_rounds)
for g in range(n_of_groups):
    plt.plot(t,sizes[g])
plt.show()
    

 """























""" sizes = []

groups = headers.initialize_game(n_of_groups, n_of_agents)

for group in groups:
    sizes.append([])


for i in range(n_of_rounds):
    headers.play_game(groups)
    
    for g in range(len(groups)):
        sizes[g].append(groups[g]["size"])

plt.plot(sizes[0])
     """

