from DAL.DB_Connection import execute
from DAL.contrrolers.agent import AgentContrroler
from models.agent import Agent

class AgentApp():
    all_agents = []
    @staticmethod
    def run_program():
        print("Welcome to agent managing system!")
        print("Please choose a number between 1-6")
        
        while True:
            AgentApp._print_menu()
            choice = input()
            is_valid = AgentApp._validate_choise(choice)
            if is_valid:
                num = int(choice)

                if num == 1:
                    AgentApp.all_agents_choice()
                elif num == 2:
                    AgentApp.add_agent_choice()
                elif num == 3:
                    pass
                elif num == 4:
                    pass
                elif num == 5:
                    pass
                else:
                    break
            

    @staticmethod
    def _print_menu():
        print("1. Get all agents")
        print("2. Add agent")
        print("3. Delete agent")
        print("4. Update agent")
        print("5. Get agent")
        print("6. Exit")

    @staticmethod
    def _validate_choise(choice):
        try:
            num = int(choice)
            if 1 <= num <= 6:
                return True
            print("Incurrect choice, please select a number (1 - 6)")
            return False
        except ValueError:
            print("Incurrect input, please enter a valid number.")
            return False
        
    def all_agents_choice():
        if AgentApp.all_agents:
            print(AgentApp.all_agents)
        else:
            agents = AgentContrroler.get_all_agents()
            if agents:
                print(agents)
            else:
                print("Agents not found.")

    def add_agent_choice():
        code_name = input("Plese enter a code name: ")
        real_name = input("Plese enter a real name: ")
        location = input("Plese enter a location: ")
        status = input("Plese enter a status (Active, Injured, Missing, Retired): ")
        params = (code_name, real_name, location, status, 0)
        agent = Agent(*params)
        AgentApp.all_agents.append(agent)
        response = AgentContrroler.add_agent(params)
        print("response", response)



if __name__ == "__main__":
    AgentApp.run_program()