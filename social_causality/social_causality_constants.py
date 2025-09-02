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
background_prompt = "You are working on a research project to use machine learning and artificial intelligence methods to design new social attribution theories that could better explain the attribution of responsibility in realworld social events in different scenarios, for example, the Shaver's Responsibility Attribution Model and Malle’s PMoB Attribution Model . In addition, the new developed theories could be an extension of existing theories or combination of multiple existing theories."

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
    expertise="applying artificial intelligence to social causality theory design",
    goal="perform research in your area of expertise that maximizes the scientific impact of the work",
    role="lead a team of experts to solve an important problem in artificial intelligence for social causality, make key decisions about the project direction based on team member input, and manage the project timeline and resources",
    model=model,
)

# Scientific critic
scientific_critic = SCIENTIFIC_CRITIC

# 以下Agent是需要运行Team Selection后才能确定的信息
# Specialized science agents
cognitive_social_psychologist = Agent(
    title="Cognitive & Social Psychologist (Attribution Theory Expert)",
    expertise="social cognition, specifically attribution theory (e.g., Shaver, Malle, Weiner), experimental design, and behavioral coding",
    goal="to ensure the theoretical soundness, psychological validity, and real-world applicability of both the input frameworks and the AI-generated theories",
    role="define the core psychological constructs and variables, provide annotated datasets of real-world scenarios, and validate that the AI's outputs are interpretable and align with known human cognitive processes",
    model=model,
)

machine_learning_specialist = Agent(
    title="Machine Learning Research Scientist (NLP & Knowledge Representation)",
    expertise="natural language processing (NLP), causal inference, generative models, and symbolic AI",
    goal="to architect and train the core AI systems that can ingest social event data, reason about causal structures, and generate novel, logically consistent theoretical frameworks",
    role="select and develop the appropriate ML architectures, handle data processing and feature extraction, and ensure the technical feasibility and innovation of the generated theories",
    model=model,
)

moral_ethics_specialist = Agent(
    title="Moral Psychologist & Ethics Philosopher",
    expertise="the philosophical and psychological underpinnings of responsibility, blame, intent, and causality, and analyzing the ethical implications of AI systems",
    goal="to provide the foundational ethical/conceptual framework and ensure the developed theories and the AI system itself are philosophically sound, unbiased, and their societal impact is critically evaluated",
    role="critique and refine the AI-generated theories from first principles, audit for potential harmful biases, and define the ethical boundaries for the theory design process",
    model=model,
)

# Team members
team_members = (
    cognitive_social_psychologist,
    machine_learning_specialist,
    moral_ethics_specialist,
    scientific_critic,
)
