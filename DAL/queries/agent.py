
class AgentQueries():
    def _get_all_agents():
        return "SELECT * FROM agents"

    def _get_agent(id):
        return f"SELECT * FROM agents WHERE id = {id}"

    def _add_agent(agent):
        return f"INSERT INTO agents (id, codeName, realName, location, status, missionsCompleted) VALUES ({agent._id}, {agent._code_name}, {agent._real_name}, {agent._location}, {agent._status}, {agent._missions_completed})"

    def _delete_agent(id):
        return f"DELETE FROM agents WHERE id = {id}"

    def _update_agent(agent):
        return f"UPDATE agents SET codeName = {agent._code_name}, realName = {agent._real_name}, location = {agent._location}, status = {agent._status}, missionsCompleted = {agent._missions_completed} WHERE id = {agent._id} "