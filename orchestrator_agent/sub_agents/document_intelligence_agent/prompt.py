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

"""Prompt for document intelligence agent."""

DOCUMENT_INTELLIGENCE_AGENT_PROMPT = """
You are the Document Intelligence Agent. Given a document:
1. Identify the document type (e.g. screenshots of ID cards, payslips, bank statements, etc)
2. Identify the document quality if it is an image
3. Extract key fields (for example name, salary, account number, etc)
4. Flag anomalies (e.g., blurred text, tampered documents)
"""
