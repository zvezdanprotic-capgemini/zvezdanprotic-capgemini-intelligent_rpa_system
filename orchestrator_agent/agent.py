# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Orchestrator agent for evaluating client loan applications."""

from google.adk.agents import SequentialAgent

from .sub_agents.insights import insights_agent
from .sub_agents.logger import logger_agent
from .sub_agents.decision_executor import decision_executor_agent
from .sub_agents.ui_context import ui_context_agent

import logging
import google.cloud.logging

logging.basicConfig()

cloud_logging_client = google.cloud.logging.Client()
cloud_logging_client.setup_logging()

orchestrator_agent = SequentialAgent(
    name='orchestrator_agent',
    description=(
        'Evaluates LLM-generated answers, verifies actual accuracy using the'
        ' web, and refines the response to ensure alignment with real-world'
        ' knowledge.'
    ),
    sub_agents=[insights_agent, logger_agent, decision_executor_agent, ui_context_agent]
)

root_agent = orchestrator_agent
