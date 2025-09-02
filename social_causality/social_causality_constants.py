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
background_prompt = "You are working on a research project to use machine learning and artificial intelligence methods to design new social causality theories that could better explain the social causality of humans in realworld in different scenarios. In addition, the new developed theories could be an extension of existing theories or combination of multiple existing theories."

#nanobody_prompt = "Your team previous decided to modify existing nanobodies to improve their binding to the newest variant of the SARS-CoV-2 spike protein."
social_causality_prompt = "NA"


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
    expertise="applying artificial intelligence to social causality theory design",
    goal="perform research in your area of expertise that maximizes the scientific impact of the work",
    role="lead a team of experts to solve an important problem in artificial intelligence for social causality, make key decisions about the project direction based on team member input, and manage the project timeline and resources",
    model=model,
)

# Scientific critic
scientific_critic = SCIENTIFIC_CRITIC

# 以下Agent是需要运行Team Selection后才能确定的信息
# Specialized science agents
immunologist = Agent(
    title="Immunologist",
    expertise="antibody engineering and immune response characterization",
    goal="guide the development of antibodies/nanobodies that elicit a strong and broad immune response",
    role="advise on immunogenicity, cross-reactivity with other variants, and potential for therapeutic application, ensuring the designs are viable for experimental validation and downstream applications",
    model=model,
)

machine_learning_specialist = Agent(
    title="Machine Learning Specialist",
    expertise="developing algorithms for protein-ligand interactions and optimization",
    goal="create and apply machine learning models to predict antibody efficacy and optimize binding affinity across SARS-CoV-2 variants",
    role="lead the development of AI tools for predicting interactions and refining antibody designs based on computational results",
    model=model,
)

computational_biologist = Agent(
    title="Computational Biologist",
    expertise="protein structure prediction and molecular dynamics simulations",
    goal="develop predictive models to identify potential antibody/nanobody candidates and simulate interactions with the SARS-CoV-2 spike protein",
    role="provide insights into structural dynamics, guide virtual screening efforts, and validate computational predictions with simulations",
    model=model,
)

# Team members
team_members = (
    immunologist,
    machine_learning_specialist,
    computational_biologist,
    scientific_critic,
)
