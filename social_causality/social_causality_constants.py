"""Constants for the social causality theory design project."""

from pathlib import Path

from virtual_lab.agent import Agent
from virtual_lab.prompts import SCIENTIFIC_CRITIC

# Meetings constants
num_iterations = 3
num_rounds = 3

# Models
#model = "gpt-4o"
model = "deepseek-chat"

model_mini = "gpt-4o-mini"


# Discussion paths
discussions_dir = Path("discussions")
workflow_phases = [
    "team_selection",
    "project_specification",
    "tools_selection",
    "implementation_agent_selection",
#    "esm",
#    "alphafold",
#    "rosetta",
    "workflow_design",
]
ablations_phases = ["ablations"]
human_eval_phases = ["human_eval"]
finetuning_phases = ["finetuning"]
review_phases = ["unpaired_cysteine"]
phases = workflow_phases + ablations_phases + human_eval_phases + finetuning_phases + review_phases
discussions_phase_to_dir = {phase: discussions_dir / phase for phase in phases}

# Prompts
#background_prompt = "You are working on a research project to use machine learning to develop antibodies or nanobodies for the newest variant of the SARS-CoV-2 spike protein that also, ideally, have activity against other circulating minor variants and past variants."

#background_prompt = "You are working on a research project to use machine learning and artificial intelligence methods to design new social attribution theories that could better explain the attribution of responsibility in realworld social events in different scenarios, for example, the Shaver's Responsibility Attribution Model and Malle’s PMoB Attribution Model . In addition, the new developed theories could be an extension of existing theories or combination of multiple existing theories."

background_prompt = "You are working on a research project using machine learning and artificial intelligence methods to test whether the responsibility attribution behavior of LLMs aligns with existing social attribution theories, specifically, Malle’s PMoB Attribution Model, a type of theory of blame. For LLMs, the attribution process of responsibility can be obtained by the chain-of-thought prompting."


#nanobody_prompt = "Your team previous decided to modify existing nanobodies to improve their binding to the newest variant of the SARS-CoV-2 spike protein."
social_attribution_prompt = "NA"


# Set up agents

# Generic agent
generic_agent = Agent(
    title="Assistant",
    expertise="helping people with their problems",
    goal="help people with their problems",
    role="help people with their problems",
    model=model,
)

# Generic team lead
generic_team_lead = Agent(
    title=f"{generic_agent.title} Lead",
    expertise=generic_agent.expertise,
    goal=generic_agent.goal,
    role=generic_agent.role,
    model=model,
)

# Generic team
generic_team = [
    Agent(
        title=f"{generic_agent.title} {i}",
        expertise=generic_agent.expertise,
        goal=generic_agent.goal,
        role=generic_agent.role,
        model=model,
    )
    for i in range(1, 5)
]

# Team lead
principal_investigator = Agent(
    title="Principal Investigator",
    expertise="artificial intelligence, computational social science, and social attribution theories",
    goal="perform research in your area of expertise that maximizes the scientific impact of the work",
    role="lead a team of experts to validate whether the responsibility attribution behavior of LLMs aligns with existing social attribution theories, make key decisions about the project direction based on team member input, and manage the project timeline and resources",
    model=model,
)

# Scientific critic
scientific_critic = SCIENTIFIC_CRITIC

# 以下Agent是需要运行Team Selection后才能确定的信息
# Specialized science agents
computational_social_scientist = Agent(
    title="Computational Social Scientist",
    expertise="formalizing psychological theories into computational models, experimental design for testing human vs. algorithmic behavior, statistical analysis of qualitative social data",
    goal="to bridge the gap between social theory and computational methods, ensuring the experimental design is both psychologically valid and methodologically sound",
    role="translate Malle's PMoB model into testable computational metrics, design the experimental vignettes/scenarios, and co-analyze the results for theoretical interpretability",
    model=model,
)

llm_research_specialist = Agent(
    title="LLM Research & Prompting Specialist",
    expertise="advanced prompt engineering (chain-of-thought, reason-act), mechanistic interpretability of transformer-based models, benchmarking and evaluating LLM behavior",
    goal="to develop robust, unbiased prompting strategies to accurately elicit and capture the LLM's internal attribution reasoning process",
    role="design and implement the chain-of-thought prompting strategies, manage the LLM API interactions, and develop the pipeline for extracting structured data from free-text responses",
    model=model,
)

data_scientist = Agent(
    title="Data Scientist & Quantitative Methodologist",
    expertise="statistical analysis of complex datasets, design of experiments (DoE), developing quantitative metrics for model evaluation, hypothesis testing",
    goal="to design the statistical framework to rigorously compare the LLM's outputs against theoretical benchmarks and ensure results are significant",
    role="develop computational metrics to quantify 'alignment', perform all statistical tests, and analyze the results to determine the degree of fit (or divergence) with PMoB",
    model=model,
)

# Team members
team_members = (
    computational_social_scientist,
    llm_research_specialist,
    data_scientist,
    scientific_critic,
)
