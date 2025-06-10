# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.runtimes.builder import RuntimeBuilder

from digitalhub_runtime_container.runtimes.runtime import RuntimeContainer


class RuntimeContainerBuilder(RuntimeBuilder):
    """RuntaimeContainerBuilder class."""

    RUNTIME_CLASS = RuntimeContainer
