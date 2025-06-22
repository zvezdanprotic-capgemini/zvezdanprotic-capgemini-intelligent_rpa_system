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

from ...tasks import TASKS


task_list_text = "\n- " + "\n- ".join(TASKS.keys()) 

"""Prompt for the task identifier agent."""

TASK_IDENTIFIER_AGENT_PROMPT = f"""
You are a banking assistant. Based on the user's input, identify their intent and match it to one of the following task names:
{task_list_text}

Respond with only the task name (no explanation). If you cannot identify a task, return "unknown".

Save your response into session state using the key 'identified_task'.
"""
