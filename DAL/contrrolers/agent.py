from DAL.queries.agent import AgentQueries
from DAL.DB_Connection import execute


class AgentContrroler():

    def get_all_agents():
        return execute(AgentQueries._get_all_agents())
    
    def get_agent(params):
        return execute(AgentQueries._get_agent(), params)
    
    def add_agent(params):
        return execute(AgentQueries._add_agent(), params)

    def update_agent(params):
        return execute(AgentQueries._update_agent(), params)

    def delete_agent(params):
        return execute(AgentQueries._delete_agent(), params)

