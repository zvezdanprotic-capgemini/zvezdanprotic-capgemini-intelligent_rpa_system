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

from .sub_agents.ui_capture_agent import ui_capture_agent
from .sub_agents.document_intelligence_agent import document_intelligence_agent

import logging
import google.cloud.logging

logging.basicConfig()

cloud_logging_client = google.cloud.logging.Client()
cloud_logging_client.setup_logging()

orchestrator_agent = SequentialAgent(
    name='orchestrator_agent',
    description="You are the Banking workflow Orchestrator. Direct the user submitted task to the specialized agents.",
    instruction="""
        """,
    sub_agents=[ui_capture_agent, document_intelligence_agent]
)

root_agent = orchestrator_agent
