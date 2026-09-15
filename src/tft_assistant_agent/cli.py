"""Command-line entry point."""

import argparse
import logging
from collections.abc import Sequence
from typing import Optional

from .agent import Agent, Message
from .config import load_settings


class EchoModel:
    """Local placeholder until a real model adapter is added."""

    def complete(self, messages: Sequence[Message]) -> str:
        user_message = next(message for message in reversed(messages) if message.role == "user")
        return f"[local echo] {user_message.content}"


def main(argv: Optional[Sequence[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Run the TFT assistant agent")
    parser.add_argument("message", help="Message to send to the agent")
    args = parser.parse_args(argv)

    settings = load_settings()
    logging.basicConfig(level=settings.log_level, format="%(levelname)s %(message)s")
    agent = Agent(model=EchoModel(), system_prompt=settings.system_prompt)
    print(agent.run(args.message))


if __name__ == "__main__":
    main()
