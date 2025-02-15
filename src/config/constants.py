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
    IDEATION_SWOT_STRENGTHS = (
        "This is a Startup. You will analyze the Strengths of the given idea. "
        "Identify key internal advantages, unique capabilities, and competitive edges "
        "that set this startup apart in the market."
    )
    IDEATION_SWOT_WEAKNESSES = (
        "This is a Startup. You will analyze the Weaknesses of the given idea. "
        "Identify internal limitations, potential risks, and areas that require improvement "
        "for the startup to succeed."
    )
    IDEATION_SWOT_OPPORTUNITIES = (
        "This is a Startup. You will analyze the Opportunities for the given idea. "
        "Identify external factors, market trends, technological advancements, "
        "or gaps in the industry that the startup can leverage for growth."
    )
    IDEATION_SWOT_THREATS = (
        "This is a Startup. You will analyze the Threats to the given idea. "
        "Identify external challenges, industry competition, regulatory hurdles, "
        "or market risks that could impact the startup's success."
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
    

class User(BaseModel):
    name: str
    password: str