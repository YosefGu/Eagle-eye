from queries.agent import AgentQueries
from DB_Connection import execute


class AgentContrroler():

    def get_all_agents():
        return execute(AgentQueries._get_all_agents())
    
    def get_agent(id):
        return execute(AgentQueries._get_agent(id))
    
    def add_agent(agent):
        return execute(AgentQueries._add_agent(agent))

    def update_agent(agent):
        return execute(AgentQueries._update_agent(agent))

    def delete_agent(id):
        return execute(AgentQueries._delete_agent(id))

