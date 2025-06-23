import logging
from .tasks import TASKS

from google.adk.agents import BaseAgent, LlmAgent
from typing import AsyncGenerator
from pydantic import BaseModel, Field
from typing_extensions import override
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event

# --- Configure Logging ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BankingWorkflowAgent(BaseAgent):
    """
    Custom orchestrator agent for banking workflows.
    This agent orchestrates a sequence of LLM agents to talk to the user, identify task, fetch task steps, 
    and invokes relevant sub-agents.
    """
    task_identifier: LlmAgent
    ui_capture_agent: LlmAgent
    document_intelligence_agent: LlmAgent

    model_config = {"arbitrary_types_allowed": True}

    def __init__(
        self,
        name: str,
        task_identifier_agent: LlmAgent,
        ui_capture_agent: LlmAgent,
        document_intelligence_agent: LlmAgent,
    ):
        super().__init__(
            name=name,
            task_identifier=task_identifier_agent,
            ui_capture_agent=ui_capture_agent,
            document_intelligence_agent=document_intelligence_agent,
            sub_agents=[task_identifier_agent, ui_capture_agent, document_intelligence_agent],
        )

    @override
    async def _run_async_impl(
        self, ctx: InvocationContext
    ) -> AsyncGenerator[Event, None]:
        
        # 1. Ask user about their task
        logger.info(f"[{self.name}] Identifying user intent...")
        async for event in self.task_identifier.run_async(ctx):
            logger.info(f"[{self.name}] Task Identification: {event}")
            yield event


        task = ctx.session.state.get("identified_task")
        if not task:
            logger.error(f"[{self.name}] Could not identify task.")
            return

        logger.info(f"[{self.name}] Task identified: {task}")

        # 2. Fetch process steps
        steps = TASKS.get(task)
        if not steps:
            logger.warning(f"[{self.name}] No predefined steps found for task: {task}")
        else:
            ctx.session.state["process_steps"] = steps
            logger.info(f"[{self.name}] Loaded steps: {steps}")