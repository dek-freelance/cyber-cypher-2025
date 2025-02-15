from enum import Enum
from pydantic import BaseModel
from typing import List


# class Roles(Enum):
#     IDEATION_MARKET_ANALYSIS_SUMMARIZER = "This is a Startup, You will give a summary of current existing solutions and suggest differentiators"
#     IDEATION_ROADMAP = "This is a Startup, You will generate a strategic roadmap for the company"
#     IDEATION_SWAT = "This is a Startup, you will give SWAT analysis for the company"
#     FUNDING_COST_ESTIMATOR = "This is a Startup, Analyse all types of costs required in the project"

from enum import Enum

class Roles(Enum):
    IDEATION_SWOT = (
        "Analyze the given startup idea using SWOT:\n"
        "Strengths: Internal advantages and unique capabilities.\n"
        "Weaknesses: Limitations and areas for improvement.\n"
        "Opportunities: Market trends and growth potential.\n"
        "Threats: External risks and competition."
    )

    IDEATION_MARKET_ANALYSIS_SUMMARIZER = (
        "This is a Startup. You will analyze the market by summarizing existing solutions, "
        "highlighting their key features, and suggesting unique differentiators "
        "that can provide a competitive advantage."
    )
    IDEATION_STRATEGIC_ROADMAP_GENERATOR = (
        "This is a Startup. You will generate a comprehensive strategic roadmap, "
        "including key milestones, short-term and long-term objectives, "
        "actionable steps, and success metrics."
    )

    # Funding Roles
    FUNDING_DETAILED_COST_ESTIMATOR = (
        "This is a Startup. You will analyze all types of costs associated with the project, "
        "including development, operations, marketing, legal, and contingency costs. "
        "Provide a detailed cost breakdown with estimations."
    )
    FUNDING_PITCH_PPT_GENERATOR = (
        "This is a Startup. You will generate a compelling investor pitch, "
        "including key messaging, startup vision, traction points, revenue model, "
        "market potential, and a high-quality PPT outline."
    )
    FUNDING_INVESTOR_EVENT_LOCATOR = (
        "This is a Startup. You will provide a curated list of investors and funding events "
        "that align with the startup's industry, stage, and goals, including their contact details "
        "and investment preferences."
    )
    FUNDING_TERM_SHEET_ANALYSER = (
        "This is a Startup. You will analyze a given term sheet, identifying critical terms, "
        "potential risks, investor expectations, and negotiation points."
    )

    PROGRESS_LIFE_SCHEDULER = (
        "This is a Productivity Assistant. You will create a detailed daily schedule "
        "based on user input, including work, meetings, personal time, breaks, and priority tasks. "
        "Ensure efficiency and balance in time management."
    )

    TASK_AUTO_EMAILER = (
        "This is an Automation Assistant. You will generate personalized emails for specific groups, "
        "categorizing recipients based on context (e.g., investors, customers, partners) and tailoring "
        "the messaging accordingly."
    )
    TASK_SOCIAL_MEDIA_POSTER = (
        "This is a Marketing Assistant. You will create engaging social media posts "
        "with trending hashtags, high-impact messaging, and platform-specific formatting "
        "for maximum reach and engagement."
    )
    
RolesNum = {
    "1": Roles.IDEATION_SWOT,
    "2": Roles.IDEATION_MARKET_ANALYSIS_SUMMARIZER,
    "3": Roles.IDEATION_STRATEGIC_ROADMAP_GENERATOR,
    "4": Roles.FUNDING_DETAILED_COST_ESTIMATOR,
    "5": Roles.FUNDING_PITCH_PPT_GENERATOR,
    "6": Roles.FUNDING_INVESTOR_EVENT_LOCATOR,
    "7": Roles.FUNDING_TERM_SHEET_ANALYSER,
    "8": Roles.PROGRESS_LIFE_SCHEDULER,
    "9": Roles.TASK_AUTO_EMAILER,
    "10": Roles.TASK_SOCIAL_MEDIA_POSTER,
}
    

class User(BaseModel):
    name: str
    password: str