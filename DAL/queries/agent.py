
class AgentQueries():
    def _get_all_agents():
        return "SELECT * FROM agents"

    def _get_agent(id):
        return f"SELECT * FROM agents WHERE id = %s"

    def _add_agent():
        return f"INSERT INTO agents (codeName, realName, location, status, missionsCompleted) VALUES ( %s, %s, %s, %s, %s)"

    def _delete_agent():
        return f"DELETE FROM agents WHERE id = %s"

    def _update_agent():
        return f"UPDATE agents SET codeName = %s, realName = %s, location = %s, status = %s, missionsCompleted = %s WHERE id = %s "