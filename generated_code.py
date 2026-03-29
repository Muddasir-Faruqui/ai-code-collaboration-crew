from dataclasses import dataclass
from typing import Dict, List
from abc import ABC, abstractmethod
import asyncio
import sys
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class Assistant:
    name: str
    description: str

@dataclass
class Task:
    id: int
    name: str
    description: str
    priority: int

@dataclass
class Response:
    message: str
    tasks: List[Task]

class BaseService(ABC):
    @abstractmethod
    def get_assistants(self) -> List[Assistant]:
        pass

    @abstractmethod
    def get_tasks(self) -> List[Task]:
        pass

class AssistantService(BaseService):
    def get_assistants(self) -> List[Assistant]:
        return [
            Assistant(name="Alice", description="Personal assistant"),
            Assistant(name="Bob", description="General assistant"),
        ]

    def get_tasks(self) -> List[Task]:
        return [
            Task(id=1, name="Buy milk", description="Buy 2 liters", priority=1),
            Task(id=2, name="Do laundry", description="Wash, dry, and fold", priority=3),
        ]

class TaskService(BaseService):
    def get_tasks(self) -> List[Task]:
        return [
            Task(id=1, name="Buy milk", description="Buy 2 liters", priority=1),
            Task(id=2, name="Do laundry", description="Wash, dry, and fold", priority=3),
        ]

def log_message(message: str) -> None:
    logger.info(message)

async def get_assistants() -> List[Assistant]:
    assistant_service = AssistantService()
    return await asyncio.to_thread(assistant_service.get_assistants)

async def get_tasks() -> List[Task]:
    task_service = TaskService()
    return await asyncio.to_thread(task_service.get_tasks)

async def handle_request() -> Response:
    log_message("Received request")
    assistants = await get_assistants()
    tasks = await get_tasks()
    return Response(
        message="Assistants and tasks retrieved successfully.",
        tasks=tasks,
    )

async def main() -> None:
    try:
        response = await handle_request()
        print(response.message)
        print(response.tasks)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())