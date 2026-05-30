import requests
from rich.console import Console
from rich.table import Table
from datetime import datetime

console = Console()

def get_weather(city="Moscow"):
    # Здесь можно добавить реальный API, но для примера — мок
    console.print(f"[bold cyan]Погода в {city}[/bold cyan]")
    console.print("[green]☀️  +24°C[/green]  Ясно")
    console.print("[yellow]Влажность: 45%  Ветер: 3 м/с[/yellow]")

if __name__ == "__main__":
    get_weather()