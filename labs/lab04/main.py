"""Точка входу для Лабораторної роботи №4 «Анімація», варіант 1."""

import argparse

import task1
import task2
import task3

TASKS = {
    "task1": task1.run,
    "task2": task2.run,
    "task3": task3.run,
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Лабораторна №4 — Анімація")
    parser.add_argument("task", choices=TASKS, help="завдання для запуску")
    arguments = parser.parse_args()
    TASKS[arguments.task]()


if __name__ == "__main__":
    main()
