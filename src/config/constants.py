from enum import Enum
from pydantic import BaseModel
from typing import List

class Roles(Enum):
    IDEATION_MARKET_ANALYSIS_SUMMARIZER = "This is a Startup, You will give a summary of current existing solutions and suggest differentiators"
    IDEATION_ROADMAP = "This is a Startup, You will generate a strategic roadmap for the company"
    IDEATION_SWAT = "This is a Startup, you will give SWAT analysis for the company"
    FUNDING_COST_ESTIMATOR = "This is a Startup, Analyse all types of costs required in the project"
    

class User(BaseModel):
    name: str
    password: str