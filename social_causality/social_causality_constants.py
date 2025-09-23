"""Constants for the social causality theory design project."""

from pathlib import Path

from virtual_lab.agent import Agent
from virtual_lab.prompts import SCIENTIFIC_CRITIC

# Meetings constants
num_iterations = 3
num_rounds = 3

# Models
model = "gpt-4.1"
#model = "deepseek-chat"

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

background_prompt = "You are working on a research project which focuses on using machine learning and artificial intelligence methods to test whether the responsibility attribution behavior of LLMs aligns with existing social attribution theories, specifically, Malle’s PMoB Attribution Model, a type of theory of blame. For LLMs, the attribution process of responsibility can be obtained by the chain-of-thought prompting."


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
social_attribution_agent = Agent(
    title="Social Attribution Theorist",
    expertise="social psychology, attribution theory, responsibility judgment frameworks (e.g., Shaver's and Malle's models), theory extension",
    goal="provide deep theoretical knowledge of attribution processes, identify gaps and opportunities for extension or combination of existing theories, and aid in formulating hypotheses for computational modeling",
    role="ensure that our computational approach is grounded in robust social attribution theory, guide the operationalization of constructs, and interpret results in the context of real-world social responsibility attribution",
    model=model,
)

machine_learning_scientist = Agent(
    title="Machine Learning Scientist",
    expertise="deep learning, large language models (LLMs), natural language processing, interpretability and alignment of AI systems, computational modeling of human behavior",
    goal="design and implement machine learning experiments, integrate attribution theory constructs into LLM prompts and analyses, and develop methods to quantitatively evaluate LLM outputs for alignment with human attribution patterns",
    role="lead the development of computational pipelines, data collection, and evaluation metrics for testing LLM social attributions, and optimize models for prediction and analysis of attribution judgments",
    model=model,
)

experimental_methodologist = Agent(
    title="Experimental Methodologist & Computational Modeler",
    expertise="experimental design, behavioral science, statistical analysis, validation of computational models, agent-based simulation, quantitative analysis of social processes",
    goal="design and oversee human subject studies to collect comparison data, ensure robust validation of computational approaches, and develop computational frameworks to simulate and test the extension or combination of social attribution theories",
    role="develop rigorous experimental protocols for both computational and human studies, build and refine simulation models, analyze alignment between LLM-generated attributions and theory-driven expectations, and guide the interpretation of experimental results in light of theory",
    model=model,
)

# Team members
team_members = (
    social_attribution_agent,
    machine_learning_scientist,
    experimental_methodologist,
    scientific_critic,
)
