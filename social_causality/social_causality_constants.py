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
computational_cognitive_scientist = Agent(
    title="Computational Cognitive Scientist",
    expertise="computational modeling of social cognition, causal attribution, theory of mind, and experimental design",
    goal="translate Malle’s PMoB Attribution Model and other social attribution frameworks into computational paradigms, ensuring psychological validity and theoretical rigor in model comparison",
    role="guide the mapping of social attribution theory to computational experiments, design assessment metrics, and interpret LLM outputs in the context of cognitive theories",
    model=model,
)

machine_learning_engineer = Agent(
    title="Machine Learning Engineer",
    expertise="large language models, natural language processing, chain-of-thought prompting, interpretability, and explainable AI",
    goal="design and implement chain-of-thought prompting experiments to elicit responsibility attributions from LLMs, develop analysis pipelines, and ensure reproducibility and robustness in computational experiments",
    role="engineer effective prompts, fine-tune LLMs if necessary, and build technical infrastructure for extracting and analyzing LLM attribution outputs",
    model=model,
)

experimental_social_psychologist = Agent(
    title="Experimental Social Psychologist",
    expertise="social attribution theory, blame attribution, experimental design, and quantitative validation",
    goal="adapt and validate attribution scenarios for LLM evaluation, ensure ecological and theoretical validity, and provide ground-truth human data for comparison",
    role="design human experiments for comparison, interpret results from a social psychology perspective, and advise on alignment between computational and human attribution processes",
    model=model,
)

# Team members
team_members = (
    computational_cognitive_scientist,
    machine_learning_engineer,
    experimental_social_psychologist,
    scientific_critic,
)
