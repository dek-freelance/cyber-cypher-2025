from src.backend.groq_chat import req_groq_langchain
from src.config.constants import Roles

def main():
    req_groq_langchain(Roles.FUNDING_COST_ESTIMATOR, "I am starting a facebook clone called netbox")
    
if __name__ == "__main__":
    main()
