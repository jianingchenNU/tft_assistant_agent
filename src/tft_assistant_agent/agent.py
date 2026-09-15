"""Small provider-agnostic agent core."""

from dataclasses import dataclass
from typing import Protocol, Sequence


@dataclass(frozen=True)
class Message:
    role: str
    content: str


class Model(Protocol):
    """The minimal interface required by :class:`Agent`."""

    def complete(self, messages: Sequence[Message]) -> str:
        ...


@dataclass
class Agent:
    model: Model
    system_prompt: str = "You are a helpful TFT assistant."

    def run(self, user_input: str) -> str:
        """Run one request through the configured model."""

        messages = (
            Message(role="system", content=self.system_prompt),
            Message(role="user", content=user_input),
        )
        return self.model.complete(messages)
