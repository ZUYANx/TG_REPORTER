import requests
import random
from random import randint
from faker import Faker
from user_agent import generate_user_agent as ua
from rich.console import Console
from rich.panel import Panel
from rich import print

console = Console()
fake = Faker()

def fake_name():
    first = fake.first_name()
    last = fake.last_name()
    return first, last

def TG_REPORT():
    console.print(Panel("[bold cyan]</> TELEGRAM REPOTER BY ZUYAN </>[/bold cyan]", expand=False))
    print("[green]" + "-" * 40 + "[/green]")
    username = console.input("[bold yellow]</> Enter terget (with @): [/bold yellow]")
    url = 'https://telegram.org/support'
    session = requests.Session()
    session.get(url)
    stel = session.cookies.get('stel_ssid', '')
    while True:
        try:
            email = fake.email()
            name = random.choice(fake_name())
            phone = "+88018" + "".join([str(randint(0, 9)) for _ in range(8)])
            message = (
                f"Hello sir/ma'am, I would like to report a Telegram user who is engaging in suspicious activity. "
                f"Their username is {username}. It seems they are attempting to deceive other users, and I believe "
                f"they are involved in scams or phishing. I request you to look into their account and take necessary action.\n\n"
                "Thank you for your assistance in ensuring a safe community."
            )
            data = {
                "message": message,
                "legal_name": name,
                "email": email,
                "phone": phone,
                "setln": ""
            }
            header = {
                "authority": "telegram.org",
                "origin": "https://telegram.org",
                "content-type": "application/x-www-form-urlencoded",
                "user-agent": ua(),
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
                "referer": "https://telegram.org/support",
                "cookie": f"stel_ssid={stel}"
            }
            req = session.post(url, headers=header, data=data).text
            if 'Thanks' in req or 'thank you' in req.lower():
                console.print(f"[bold green]</> Report Successful! Email used:[cyan]{email}[/cyan][/bold green]")
            else:
                console.print(f"[bold red]Report Failed! Email used: [cyan]{email}[/cyan][/bold red]")
        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {e}")

TG_REPORT()