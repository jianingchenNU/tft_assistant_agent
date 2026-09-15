import unittest

from tft_assistant_agent.agent import Agent, Message


class RecordingModel:
    def __init__(self) -> None:
        self.messages = ()

    def complete(self, messages: tuple[Message, ...]) -> str:
        self.messages = messages
        return "ok"


class AgentTests(unittest.TestCase):
    def test_run_builds_system_and_user_messages(self) -> None:
        model = RecordingModel()
        result = Agent(model, system_prompt="Be concise").run("hello")

        self.assertEqual(result, "ok")
        self.assertEqual(
            model.messages,
            (
                Message("system", "Be concise"),
                Message("user", "hello"),
            ),
        )


if __name__ == "__main__":
    unittest.main()
