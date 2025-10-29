# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from enum import Enum


class EntityKinds(Enum):
    """
    Entity kinds.
    """

    FUNCTION_CONTAINER = "container"
    TASK_CONTAINER_BUILD = "container+build"
    TASK_CONTAINER_JOB = "container+job"
    TASK_CONTAINER_DEPLOY = "container+deploy"
    TASK_CONTAINER_SERVE = "container+serve"
    RUN_CONTAINER_BUILD = "container+build:run"
    RUN_CONTAINER_JOB = "container+job:run"
    RUN_CONTAINER_DEPLOY = "container+deploy:run"
    RUN_CONTAINER_SERVE = "container+serve:run"


class Actions(Enum):
    """
    Task actions.
    """

    BUILD = "build"
    JOB = "job"
    DEPLOY = "deploy"
    SERVE = "serve"
